def load_shopping_list(filename):
    """
    Loads a shopping list from a specified file using Python's eval() function.
    
    Parameters:
        filename (str): The path to the file from which the shopping list is to be loaded.
    
    Returns:
        list or dict: The shopping list loaded from the file. The type depends on the content of the file.
    
    Raises:
        FileNotFoundError: If the specified file does not exist.
    
    Note:
        This function uses eval(), which can run arbitrary Python code. Only use it with trusted files.
    """
    try:
        with open(filename, 'r') as file:
            return eval(file.read())
    except FileNotFoundError:
        print(f"No such file: {filename}")
        return []


def save_shopping_list(shopping_list, filename):
    """
    Saves the shopping list to a specified file in a string representation.
    
    Parameters:
        shopping_list (list or dict): The shopping list to be saved. It can be any serializable structure.
        filename (str): The path to the file where the shopping list will be saved.
    
    Returns:
        None
    
    Side Effects:
        Writes to a file, potentially overwriting existing content without warning.
    
    Example:
        save_shopping_list(['apples', 'bananas'], 'list.txt')  # Saves the list to 'list.txt'
    """
    with open(filename, 'w') as file:
        file.write(str(shopping_list))
    print(f"Shopping list saved to {filename}")


def create_shopping_list(source='manual', data=None):
    """
    Creates a shopping list from various sources.
    
    Parameters:
        source (str): The source from which to create the list. Options are 'manual', 'database', or 'api'.
        data (list or dict, optional): Predefined data to load as the shopping list, used when source is 'database' or 'api'.
    
    Returns:
        tuple: A tuple containing the shopping list and a message about how the list was created.
    """
    if source == 'manual':
        return [], "Empty shopping list created manually."
    elif source == 'database':
        # Here you could connect to a database to fetch a predefined list
        return data, "Shopping list loaded from database."
    elif source == 'api':
        # Simulate fetching a shopping list from an API
        return data, "Shopping list retrieved via API."
    else:
        return [], "Source not recognized, empty list created."
    

def add_item(shopping_list, item, quantity=1):
    """
    Adds an item and its quantity to the shopping list, supporting both list and dict formats.
    
    Parameters:
        shopping_list (list or dict): The shopping list to which the item will be added.
        item (str): The item to add to the shopping list.
        quantity (int): The quantity of the item to add (default is 1).
    
    Returns:
        tuple: The updated shopping list and a message indicating the item was added.
    """
    if isinstance(shopping_list, list):
        shopping_list.append((item, quantity))
    elif isinstance(shopping_list, dict):
        shopping_list[item] = shopping_list.get(item, 0) + quantity
    return shopping_list, f"Added {quantity} {item}(s) to the shopping list."


def remove_item(shopping_list, item):
    """
    Removes an item from the shopping list. Supports removing multiple items if a list of items is provided.
    
    Parameters:
        shopping_list (dict): The shopping list from which the item will be removed.
        item (str or list): The item or list of items to remove.
    
    Returns:
        tuple: The updated shopping list and a message indicating the items were removed.
    """
    if isinstance(item, list):
        for i in item:
            shopping_list.pop(i, None)
        return shopping_list, f"Multiple items removed."
    else:
        shopping_list.pop(item, None)
        return shopping_list, f"{item} removed from the shopping list."


def check_item_availability(item, cache={}):
    """
    Checks item availability using a cache to reduce load on database or API.
    
    Parameters:
        item (str): The item to check availability for.
        cache (dict, optional): A cache to store previous availability checks.
    
    Returns:
        tuple: A boolean indicating if the item is available and a message about the check.
    """
    if item in cache:
        return cache[item], "Checked from cache."
    else:
        # Simulated API call
        availability = True  # Example logic
        cache[item] = availability
        return availability, "Checked from API and cached."


def calculate_total_cost(shopping_list, tax_rate=0.07, discount=0, promo_code=None):
    """
    Calculates the total cost of the shopping list including tax, discount, and optional promo codes.
    
    Parameters:
        shopping_list (dict): The shopping list with items and quantities.
        tax_rate (float): Tax rate to apply to the subtotal.
        discount (float): Flat discount amount to apply.
        promo_code (str, optional): Promo code that might apply additional discounts.
    
    Returns:
        tuple: The total cost and a detailed breakdown of the calculation.
    """
    prices = {'Bread': 200, 'Milk': 150, 'Eggs': 50}
    subtotal = sum(quantity * prices.get(item, 100) for item, quantity in shopping_list.items())
    if promo_code == "SAVE10":
        discount += 10  # Additional 10 unit discount
    tax = subtotal * tax_rate
    total_cost = subtotal + tax - discount
    return total_cost, f"Subtotal: {subtotal}, Tax: {tax}, Discount: {discount}, Total: {total_cost}"


def go_to_checkout(queue_length, current_time):
    """
    Estimates wait time at checkout based on queue length and current time factors.
    
    Parameters:
        queue_length (int): The number of people in line at checkout.
        current_time (str): Current part of the day ('morning', 'lunch', 'evening').
    
    Returns:
        tuple: Estimated wait time in minutes and a message describing the wait time.
    """
    base_time = queue_length * 2
    if current_time in ['lunch', 'evening']:
        wait_time = base_time * 1.5  # Longer wait times during peak hours
    else:
        wait_time = base_time
    return wait_time, f"Estimated wait time is {wait_time} minutes."


def pay_for_purchases(amount, payment_type='cash'):
    """
    Processes payment and verifies transaction success.
    
    Parameters:
        amount (float): The amount to be paid.
        payment_type (str): Method of payment (e.g., 'cash', 'credit_card').
    
    Returns:
        tuple: None if transaction fails, or the amount paid and a success message.
    """
    if payment_type == 'credit_card' and amount > 500:
        return None, "Transaction failed: credit limit exceeded."
    return amount, f"Paid {amount} using {payment_type}, transaction successful."


def take_receipt(email=None, receipt_type='paper'):
    """
    Issues a receipt, optionally by email.
    
    Parameters:
        email (str, optional): The email address to send an electronic receipt to.
        receipt_type (str): The type of receipt to issue ('paper', 'email').
    
    Returns:
        str: A message indicating how the receipt was issued.
    """
    if email and receipt_type == 'email':
        return f"Receipt emailed to {email}."
    return "Physical receipt issued."


def pack_purchases(pack_type='paper'):
    """
    Packs purchases into specified types of bags.
    
    Parameters:
        pack_type (str): The type of packing material ('paper', 'plastic', 'eco').
    
    Returns:
        str: A message describing how the purchases were packed.
    """
    if pack_type == 'eco':
        return "Purchases have been packed in eco-friendly material."
    return f"Purchases have been packed in {pack_type} bags."


def accept_thanks(customer_name, time_of_day='morning'):
    """
    Personalizes thanks based on the customer and time of day.
    
    Parameters:
        customer_name (str): The name of the customer.
        time_of_day (str): The time of day ('morning', 'evening').
    
    Returns:
        str: A personalized thank you message.
    """
    greeting = 'Good morning' if time_of_day == 'morning' else 'Good evening'
    return f"{greeting} {customer_name}, you're welcome!"