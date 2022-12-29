# CS 421: Natural Language Processing
# University of Illinois at Chicago
# Fall 2020
# Chatbot Project - Evaluation
#
# Do not rename/delete any functions or global variables provided in this template and write your solution
# in the specified sections. Use the main function to test your code when running it from a terminal.
# Avoid writing that code in the global scope; however, you should write additional functions/classes
# as needed in the global scope. These templates may also contain important information and/or examples
# in comments so please read them carefully.
# =========================================================================================================

# Import any necessary libraries here, but check with the course staff before requiring any external
# libraries.
import re
import random
from word2number import w2n
from collections import defaultdict

dst = defaultdict(list)

# nlu(input): Interprets a natural language input and identifies relevant slots and their values
# Input: A string of text.
# Returns: A list ([]) of (slot, value) pairs.  Slots should be strings; values can be whatever is most
#          appropriate for the corresponding slot.  If no slot values are extracted, the function should
#          return an empty list.
def nlu(input=""):
    # [YOUR CODE HERE]
    global dst
    # Dummy code for sample output (delete or comment out when writing your code!):
    slots_and_values = []
    list2 = []
    # To narrow the set of expected slots, you may (optionally) first want to determine the user's intent,
    # based on what the chatbot said most recently.
    user_intent = ""
    if "dialogue_state_history" in dst:
        if dst["dialogue_state_history"][0] == "request_type":
            pattern = re.compile(r"\b([vV]eggie)|([nN]on-?\s?veg)\b")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_type"
                slots_and_values.append(("user_intent_history", "respond_type"))
                dst["user_intent_history"].append("respond_type")
            else:
                user_intent = "unknown"
                slots_and_values.append(("user_intent_history", "unknown"))
                print("Only 'veggie' or 'non-veg' is allowed for pizza type")
        
        if dst["dialogue_state_history"][0] == "request_size":
            pattern = re.compile(r"\b([Ss]mall)|([Mm]edium)|([Ll]arge)\b")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_size"
                slots_and_values.append(("user_intent_history", "respond_size"))
            else:
                user_intent = "unknown"
                slots_and_values.append(("user_intent_history", "unknown"))
                print("Only 'small' or 'medium' or 'large' is allowed for pizza type")
        
        if dst["dialogue_state_history"][0] == "request_toppings":
            pattern = re.compile(r"\b([m|M]ushrooms?)|([o|O]nions?)|([g|G]reen peppers?)|([b|B]acon)|([p|P]epperoni)|([h|H]ot\s?[p|P]eppers?)|([o|O]lives?)\b")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_toppings"
                slots_and_values.append(("user_intent_history", "respond_toppings"))
            else:
                user_intent = "unknown"
                slots_and_values.append(("user_intent_history", "unknown"))
                print("Please choose from the available toppings: 'mushrooms', 'onions', 'green peppers', 'hot peppers', 'olives', 'bacon', 'pepperoni'")
        
        if dst["dialogue_state_history"][0] == "request_num_pizzas":
            pattern = re.compile(r"[A-Za-z0-9]*")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_num_pizzas"
                slots_and_values.append(("user_intent_history", "respond_num_pizzas"))
            else:
                user_intent = "unknown"
                slots_and_values.append(("user_intent_history", "unknown"))
                print("Please insert a valid number either in digits or words!")
        
        if dst["dialogue_state_history"][0] == "request_clarification":
            pattern = re.compile(r"\b((y|Y)es)|((n|N)o)\b")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_clarification"
                slots_and_values.append(("user_intent_history", "respond_clarification"))
            else:
                user_intent = "unknown"
                slots_and_values.append(("user_intent_history", "unknown"))
                print("Only yes or no is allowed!")
        
        if dst["dialogue_state_history"][0] == "request_name":
            pattern = re.compile(r"^([A-Za-z]*\s[A-Za-z]*)$")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_name"
                slots_and_values.append(("user_intent_history", "respond_name"))
            else:
                user_intent = "unknown"
                slots_and_values.append(("user_intent_history", "unknown"))
                print("Please enter a first name and a last name!")
        
        if dst["dialogue_state_history"][0] == "request_phone_num":
            pattern = re.compile(r"\d{3}(\-)?\d{3}(\-)?\d{4}")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_phone_num"
                slots_and_values.append(("user_intent_history", "respond_phone_num"))
            else:
                user_intent = "unknown"
                slots_and_values.append(("user_intent_history", "unknown"))
                print("Please enter a valid 10 digit phone number!")
        
        if dst["dialogue_state_history"][0] == "request_address":
            # Check to see if the input contains a valid size.
            pattern = re.compile(r"[0-9]{1,3}.+")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_address"
                slots_and_values.append(("user_intent_history", "respond_address"))
            else:
                user_intent = "unknown"
                slots_and_values.append(("user_intent_history", "unknown"))
                print("Please enter a valid address!")
                  
        if dst["dialogue_state_history"][0] == "request_confirmation":
            # Check to see if the input contains a valid size.
            pattern = re.compile(r"([yY]es)|([nN]o)")
            match = re.search(pattern, input)
            if match:
                user_intent = "respond_confirmation"
                slots_and_values.append(("user_intent_history", "respond_confirmation"))
            else:
                user_intent = "unknown"
                slots_and_values.append(("user_intent_history", "unknown"))
                print("Please confirm your order using yes or no!")

    # If you're maintaining a dialogue state history but there's nothing there yet, this is probably the
    # first input of the conversation!
    # else:
    #     user_intent = "greeting"
    #     slots_and_values.append(("user_intent_history", "greeting"))
        
    # Then, based on what type of user intent you think the user had, you can determine which slot values
    # to try to extract.
        
    if user_intent == "respond_type":
        pattern = re.compile(r"\b([vV]eggie)\b")
        contains_veggie = re.search(pattern, input)
        pattern = re.compile(r"\b([nN]on-?\s?veg)\b")
        contains_nonveg = re.search(pattern, input)
        
        if contains_veggie:
            slots_and_values.append(("pizza_type", "veggie"))
        elif contains_nonveg:
            slots_and_values.append(("pizza_type", "non-veg"))

    if user_intent == "respond_size":
        pattern = re.compile(r"^(?!.*(m|M)edium)^(?!.*(l|L)arge).*((s|S)mall).*$")
        contains_small = re.search(pattern, input)
        
        pattern = re.compile(r"^(?!.*(s|S)mall)^(?!.*(l|L)arge).*((m|M)edium).*$")
        contains_medium = re.search(pattern, input)
        
        pattern = re.compile(r"^(?!.*(m|M)edium)^(?!.*(s|S)mall).*((l|L)arge).*$")
        contains_large = re.search(pattern, input)
        
        # Note that this if/else block wouldn't work perfectly if the input contained, e.g., both "small"
        # and "medium" ... ;)
        ###########################################
        # To prevent the mentioned problem, I used nagative lookahead to make sure only one of the allowed sizes is given by the user
        ###########################################
        if contains_small:
            slots_and_values.append(("pizza_size", "small"))
        elif contains_medium:
            slots_and_values.append(("pizza_size", "medium"))
        elif contains_large:
            slots_and_values.append(("pizza_size", "large"))
        
    if user_intent == "respond_toppings":
        # Tries to find the matches for all the allowed toppings and then append all the allowed given toppings to the dictionary
        pattern = re.compile(r"\b([m|M]ushrooms?)|([o|O]nions?)|([g|G]reen peppers?)|([b|B]acon)|([p|P]epperoni)|([h|H]ot\s?[p|P]eppers?)|([o|O]lives?)\b")
        contains_small = re.findall(pattern, input)
        
        for i in contains_small:
            for j in i:
                if j != '':
                    list2.append(j)

        slots_and_values.append(("pizza_toppings", list2))

    if user_intent == "respond_num_pizzas":
        pattern = re.compile(r"(\d+)")
        contains_num = re.search(pattern, input)
        # Looks for the digit and also if the user used alphabet to specify number of the desired pizzas

        if contains_num:
            slots_and_values.append(("num_pizzas", int(contains_num.group(1)))) 
        elif type(w2n.word_to_num(input)) == int:
            slots_and_values.append(("num_pizzas", w2n.word_to_num(input)))
        ###################
        # Commented this part since word2number library is not loaded on gradescope. However, I tested on my compter
        # and it works.
      
    if user_intent == "respond_clarification":
        pattern = re.compile(r"\b((y|Y)es)\b")
        contains_yes = re.search(pattern, input)
        
        pattern = re.compile(r"\b((n|N)o)\b")
        contains_no = re.search(pattern, input)
        
        if contains_yes:
            slots_and_values.append(("clarification", "yes"))
        elif contains_no:
            slots_and_values.append(("clarification", "no"))
            
    if user_intent == "respond_name":
        pattern = re.compile(r"^([A-Za-z]*\s[A-Za-z]*)$")
        contains_name = re.search(pattern, input)
        # First and last name separated by a space
        if contains_name:
            slots_and_values.append(("name", contains_name.group(1)))
    
    if user_intent == "respond_phone_num":
        pattern = re.compile(r"\d{3}(\-)?\d{3}(\-)?\d{4}")
        contains_phone = re.search(pattern, input)
        # 10 digit phone number in one of the following formats:
        # 1) 3121234567
        # 2) 312-1234567
        # 3) 312-123-4567
        if contains_phone:
            slots_and_values.append(("phone_num", input))
    
    if user_intent == "respond_address":
        pattern = re.compile(r"[0-9]{1,3}.+")
        contains_address = re.search(pattern, input)
        # 1 to 3 digits at the beginning and then any characters
        if contains_address:
            slots_and_values.append(("address", input))
        
    if user_intent == "respond_confirmation":
        pattern = re.compile(r"((y|Y)es)")
        contains_yes = re.search(pattern, input)
        
        pattern = re.compile(r"((n|N)o)")
        contains_no = re.search(pattern, input)

        if contains_yes:
            slots_and_values.append(("confirmation", "yes"))
        elif contains_no:
            slots_and_values.append(("confirmation", "no"))         
            
    return slots_and_values

# update_dst(input): Updates the dialogue state tracker
# Input: A list ([]) of (slot, value) pairs.  Slots should be strings; values can be whatever is
#        most appropriate for the corresponding slot.  Defaults to an empty list.
# Returns: Nothing
def update_dst(input=[]):
    global dst
    for i in input:
        if i[0] not in dst:
            if i[0] == "pizza_type":
                if re.match("(^[vV]eggie$)|(^[nN]on-veg$)", i[1]):
                    dst["pizza_type"].append(i[1])
                    print('hey hey hey')
                    dst["dialogue_state_history"].append("request_type")
                    dst["user_intent_history"].append("respond_type")
            elif i[0] == "pizza_size":
                if re.match("(^small$)|(^medium$)|(^large$)", i[1]):
                    dst["pizza_size"].append(i[1])
                    dst["dialogue_state_history"].append("request_size")
                    dst["user_intent_history"].append("respond_size")
            elif i[0] == "pizza_toppings":
                if all(re.match("(^mushrooms?$)|(^onions?$$)|(^green peppers?$)|(^bacon$)|(^pepperoni$)|(^hot peppers?$)|(^olives?$)", i) \
                       for i in i[1]) == True:
                    dst["pizza_toppings"].append(i[1])
                    dst["dialogue_state_history"].append("request_toppings")
                    dst["user_intent_history"].append("respond_toppings")
            elif i[0] == "num_pizzas":
                dst["num_pizzas"].append(i[1])   
                dst["dialogue_state_history"].append("request_num_pizzas")
                dst["user_intent_history"].append("respond_num_pizzas")
            elif i[0] == "clarification":
                if re.match("(^yes$)|(^no$)", i[1]):
                    dst["clarification"].append(i[1])
                    dst["dialogue_state_history"].append("request_clarification")
                    dst["user_intent_history"].append("respond_clarification")
            elif i[0] == "name":
                if re.match("^[A-Za-z\s]*$", i[1]):
                    dst["name"].append(i[1])
                    dst["dialogue_state_history"].append("request_name")
                    dst["user_intent_history"].append("respond_name")
            elif i[0] == "phone_num":
                if re.match("^\d{3}(\-)?\d{3}(\-)?\d{4}", str(i[1])):
                    dst["phone_num"].append(i[1])  
                    dst["dialogue_state_history"].append("request_phone_num")
                    dst["user_intent_history"].append("respond_phone_num")
            elif i[0] == "address":
                if re.match("[0-9]{1,3}.+", i[1]):
                    dst["address"].append(i[1])  
                    dst["dialogue_state_history"].append("request_address")
                    dst["user_intent_history"].append("respond_address")
            elif i[0] == "confirmation":
                if re.match("([yY]es)|([nN]o)", i[1]):
                    dst["confirmation"].append(i[1])  
                    dst["dialogue_state_history"].append("request_confirmation")
                    dst["user_intent_history"].append("respond_confirmation")
        if i[0] in dst:
            if i[0] == "pizza_type":
                if re.match("(^veggie$)|(^non-veg$)", i[1]):
                    dst["pizza_type"]=i[1]
            elif i[0] == "pizza_size":
                if re.match("(^small$)|(^medium$)|(^large$)", i[1]):
                    dst["pizza_size"]= i[1]
            elif i[0] == "pizza_toppings":
                if all(re.match("(^mushrooms?$)|(^onions?$)|(^green peppers?$)|(^bacon$)|(^pepperoni$)|(^hot peppers?$)|(^olives?$)", i) \
                       for i in i[1]) == True:
                    dst["pizza_toppings"]=i[1]
            elif i[0] == "num_pizzas":
                dst["num_pizzas"]=i[1]    
            elif i[0] == "clarification":
                if re.match("(^[yY]es$)|(^[nN]o$)", i[1]):
                    dst["clarification"]=i[1]
            elif i[0] == "name":
                if re.match("^[A-Za-z\s]*$", i[1]):
                    dst["name"]=i[1]
            elif i[0] == "phone_num":
                if re.match("\d{3}(\-)?\d{3}(\-)?\d{4}", str(i[1])):
                    dst["phone_num"]=i[1]         
            elif i[0] == "address":
                if re.match("[0-9]{1,3}.+", i[1]):
                    dst["address"]=i[1]  
            elif i[0] == "confirmation":
                if re.match("(^[yY]es$)|(^[nN]o$)", i[1]):
                    dst["confirmation"]=i[1]   
    return 

# get_dst(slot): Retrieves the stored value for the specified slot, or the full dialogue state at the
#                current time if no argument is provided.
# Input: A string value corresponding to a slot name.
# Returns: A dictionary representation of the full dialogue state (if no slot name is provided), or the
#          value corresponding to the specified slot.
def get_dst(slot=""):
    if len(slot) >= 1:
        if slot == "pizza_type" or slot == "pizza_size" or slot == "pizza_toppings" or slot == "num_pizzas" \
            or slot == "name" or slot == "phone_num" or slot == "address":
            if dst[slot]:
                a = dst[slot]
            else:
                a= "Slot is still empty!"
        else:
            a= "Slot does not exist!"        
    else:
        a = dst
    return a

# dialogue_policy(dst): Selects the next dialogue state to be uttered by the chatbot.
# Input: A dictionary representation of a full dialogue state.
# Returns: A string value corresponding to a dialogue state, and a list of (slot, value) pairs necessary
#          for generating an utterance for that dialogue state (or an empty list if no (slot, value) pairs
#          are needed).
def dialogue_policy(b=[]):
    global dst
    if not b["pizza_type"]:
        next_state = "pizza_type"
        slot_values = []
        dst["dialogue_state_history"].append("request_type")
    elif b["pizza_type"] and not b["pizza_size"]:
        next_state = "pizza_size"
        slot_values = []
        dst["dialogue_state_history"].insert(0,"request_size")
    elif b["pizza_size"] and not b["pizza_toppings"]:
        next_state = "pizza_toppings"
        slot_values = []
        dst["dialogue_state_history"].insert(0,"request_toppings")
    elif b["pizza_toppings"] and not b["num_pizzas"]:
        next_state = "num_pizzas"
        slot_values = []
        dst["dialogue_state_history"].insert(0,"request_num_pizzas")
    elif b["num_pizzas"] > 10:
        if not b["clarification"]:
            next_state = "clarification"
            slot_values = [str(b["num_pizzas"])]
            dst["dialogue_state_history"].insert(0,"request_clarification")
        elif b["clarification"] == "yes":
            if not b["name"]:
                next_state = "name"
                slot_values = []
                dst["dialogue_state_history"].insert(0,"request_name")
            elif b["name"] and not b["phone_num"]:
                next_state = "phone_num"
                slot_values = []
                dst["dialogue_state_history"].insert(0,"request_phone_num")
            elif b["phone_num"] and not b["address"]:
                next_state = "address"
                slot_values = []
                dst["dialogue_state_history"].insert(0,"request_address")
            elif b["address"] and not b["confirmation"]:
                next_state = "confirmation"
                slot_values = []
                dst["dialogue_state_history"].insert(0,"request_confirmation")
            elif b["confirmation"] == "no":
                next_state = "pizza_type"
                slot_values = []
            elif b["confirmation"] == "yes" and not b["farewell"]:
                next_state = "farewell"
                slot_values = []
        elif b["clarification"] == "no":
            next_state = "num_pizzas"
            slot_values = []
            dst["dialogue_state_history"].insert(0,"request_num_pizzas")
    elif b["num_pizzas"] <= 10 and not b["name"]:
        next_state = "name"
        slot_values = []
        dst["dialogue_state_history"].insert(0,"request_name")
    elif b["name"] and not b["phone_num"]:
        next_state = "phone_num"
        slot_values = []
        dst["dialogue_state_history"].insert(0,"request_phone_num")
    elif b["phone_num"] and not b["address"]:
        next_state = "address"
        slot_values = []
        dst["dialogue_state_history"].insert(0,"request_address")
    elif b["address"] and not b["confirmation"]:
        next_state = "confirmation"
        slot_values = []
        dst["dialogue_state_history"].insert(0,"request_confirmation")
    elif b["confirmation"] == "no":
        next_state = "pizza_type"
        slot_values = []
        dst = []
    elif b["confirmation"] == "yes" and not b["farewell"]:
        next_state = "farewell"
        slot_values = []
    return next_state, slot_values
	
# nlg(state, slots=[]): Generates a surface realization for the specified dialogue act.
# Input: A string indicating a valid state, and optionally a list of (slot, value) tuples.
# Returns: A string representing a sentence generated for the specified state, optionally
#          including the specified slot values if they are needed by the template.
def nlg(state, slots=[]):
    # [YOUR CODE HERE]
    global dst
    # Dummy code for sample output (delete or comment out when writing your code!):
    templates = defaultdict(list)
    slots_dict = dict(slots)
    
    # Build at least two templates for each dialogue state that your chatbot might use.
    # templates["greetings"] = []
    # templates["greetings"].append("Hey! Welcome to 421 Pizzeria!")
    # templates["greetings"].append("Hi! Thanks for choosing 421 Pizzeria!")
    
    templates["pizza_type"] = []
    templates["pizza_type"].append("What kind of pizza do you want?")
    templates["pizza_type"].append("Would you like veggie or non-veg pizza?")
    
    templates["pizza_size"] = []
    templates["pizza_size"].append("What size?")
    templates["pizza_size"].append("small, medium, or large?")
    
    templates["pizza_toppings"] = []
    templates["pizza_toppings"].append("What kind of pizza topping(s) would you like?")
    #templates["pizza_toppings"].append("Please choose from the available toppings: mushrooms, onions, green peppers, hot peppers, olives, bacon, pepperoni.")
    
    templates["num_pizzas"] = []
    templates["num_pizzas"].append("How many?")
    templates["num_pizzas"].append("How many pizza(s) would you like to order?")
    
    templates["clarification"] = []
    templates["clarification"].append("Just double-checking ...did you say that you want <num_pizzas> pizzas?")
    templates["clarification"].append("Just to make sure ...do you want to order <num_pizzas> pizzas?")
    
    templates["name"] = []
    templates["name"].append("Let me just take your info. What’s your name?")
    templates["name"].append("What’s your name?")
    
    templates["phone_num"] = []
    templates["phone_num"].append("Your cell number?")
    templates["phone_num"].append("What is the best phone number to reach you at?")
    
    templates["repeat"] = []
    templates["repeat"].append("Can you answer my original question in a way that I might understand it better?")
    
    templates["address"] = []
    templates["address"].append("Finally, the delivery address?")
    templates["address"].append("What's your address?")
    
    templates["confirmation"] = []
    templates["confirmation"].append("<num_pizzas> <pizza_size> <pizza_type> with <pizza_toppings>. Do you confirm this order?")
    templates["confirmation"].append("Your order summary is:<num_pizzas> <pizza_size> <pizza_type> pizzas with <pizza_toppings>. Is that correct?")
    
    templates["farewell"] = []
    templates["farewell"].append("Awesome! Your order is placed. You’ll soon get a text message when your order is ready to be delivered")
    templates["farewell"].append("Thank you for your order! We'll send you a text message when your order is ready!")
    
    # When you implement this for real, you'll need to randomly select one of the templates for
    # the specified state, rather than always selecting template 0.  You probably also will not
    # want to rely on hardcoded input slot positions (e.g., slots[0][1]).  Optionally, you might
    # want to include logic that handles a/an and singular/plural terms, to make your chatbot's
    # output more natural (e.g., avoiding "did you say you want 1 pizzas?").
    output = ""
    if state == "clarification":
        if dst["num_pizzas"] == 1:
            output = random.choice(templates[state]).replace("<num_pizzas>", str(dst["num_pizzas"]))
            output = output.replace("pizzas", "pizza")
        else:
            output = random.choice(templates[state]).replace("<num_pizzas>", str(dst["num_pizzas"]))
    elif state == "confirmation":
        output = random.choice(templates[state]).replace("<num_pizzas>", str(dst["num_pizzas"]))
        output = output.replace("<pizza_size>", dst["pizza_size"])
        output = output.replace("<pizza_type>", dst["pizza_type"])
        output = output.replace("<pizza_toppings>", ' and '.join(dst["pizza_toppings"]))
        if dst["num_pizzas"] == 1:
            output = output.replace("pizzas", "pizza")
    else:
        output = random.choice(templates[state])
    return output



# Use this main function to test your code when running it from a terminal
# Sample code is provided to assist with the assignment, feel free to change/remove it if you want
# You can run the code from terminal as: python3 chatbot.py

def main():
    
    # You can choose whether your chatbot or the participant will make the first dialogue utterance.
    # In the sample here, the chatbot makes the first utterance.
    print("Hey! Welcome to 421 Pizzeria!")
    current_state_tracker = get_dst()
    #print("1", dst)
    next_state, slot_values = dialogue_policy(current_state_tracker)
    #print("2",next_state, slot_values)
    #print("3", dst)
    output = nlg(next_state, slot_values)
    print(output)
    
    # With our first utterance complete, we'll enter a loop for the rest of the dialogue.  In some cases,
    # especially if the participant makes the first utterance, you can enter this loop directly without
    # needing the previous code block.
    while next_state != "farewell":
        # Accept the user's input.
        user_input = input()
        
        # Perform natural language understanding on the user's input.
        slots_and_values = nlu(user_input)
        #print("4",slots_and_values)
        #print("44", dst)

        
        # Store the extracted slots and values in the dialogue state tracker.
        update_dst(slots_and_values)
        #print("5",dst)
        
        # Get the full contents of the dialogue state tracker at this time.
        current_state_tracker = get_dst()
        #print("6",current_state_tracker)
        #print(dst)
        # Determine which state the chatbot should enter next.
        next_state, slot_values = dialogue_policy(current_state_tracker)
        #print("7",next_state, slot_values)
        # Generate a natural language realization for the specified state and slot values.
        output = nlg(next_state, slot_values)
        
        # Print the output to the terminal.
        print(output)
        


################ Do not make any changes below this line ################
if __name__ == '__main__':
    main()
