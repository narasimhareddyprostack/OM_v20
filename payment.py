def process_payment(amount, card_number, card_holder, cvv):
    """
    Dummy payment processing function for demonstration purposes.
    
    Args:
        amount (float): Payment amount
        card_number (str): Credit card number
        card_holder (str): Cardholder name
        cvv (str): Card verification value
    
    Returns:
        dict: Payment result with status and transaction ID
    """
    if not amount or amount <= 0:
        return {"status": "failed", "message": "Invalid amount"}
    
    if len(card_number) != 16:
        return {"status": "failed", "message": "Invalid card number"}
    
    if len(cvv) != 3:
        return {"status": "failed", "message": "Invalid CVV"}
    
    # Simulate payment processing
    transaction_id = f"TXN{card_number[-4:]}{hash(card_holder) % 10000:04d}"
    
    return {
        "status": "success",
        "transaction_id": transaction_id,
        "amount": amount,
        "card_holder": card_holder,
        "message": "Payment processed successfully"
    }


# Example usage
if __name__ == "__main__":
    result = process_payment(99.99, "1234567890123456", "John Doe", "123")
    print(result)