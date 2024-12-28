class AMM:
    """
    Automated Market Maker (AMM) implementation using the constant product formula.
    """
    def __init__(self, apples, potatoes):
        """
        Initialize the AMM with initial quantities of apples and potatoes.
        
        :param apples: Initial quantity of apples in the pool.
        :param potatoes: Initial quantity of potatoes in the pool.
        """
        self.apples = apples
        self.potatoes = potatoes
        self.k = apples * potatoes  # Constant product (x * y = k)
    
    def get_price(self):
        """
        Get the current price of 1 apple in terms of potatoes.
        Price is defined as: potatoes / apples.
        """
        return self.potatoes / self.apples
    
    def trade_apples_for_potatoes(self, apple_amount):
        """
        Simulate a trade where apples are added to the pool to get potatoes.
        
        :param apple_amount: The number of apples the user wants to trade.
        :return: The number of potatoes the user will receive.
        """
        if apple_amount <= 0:
            raise ValueError("Trade amount must be positive.")
        
        # New quantity of apples after trade
        new_apples = self.apples + apple_amount
        
        # Calculate the new quantity of potatoes to maintain k
        new_potatoes = self.k / new_apples
        
        # Potatoes received
        potatoes_received = self.potatoes - new_potatoes
        
        # Update pool state
        self.apples = new_apples
        self.potatoes = new_potatoes
        
        return potatoes_received
    
    def trade_potatoes_for_apples(self, potato_amount):
        """
        Simulate a trade where potatoes are added to the pool to get apples.
        
        :param potato_amount: The number of potatoes the user wants to trade.
        :return: The number of apples the user will receive.
        """
        if potato_amount <= 0:
            raise ValueError("Trade amount must be positive.")
        
        # New quantity of potatoes after trade
        new_potatoes = self.potatoes + potato_amount
        
        # Calculate the new quantity of apples to maintain k
        new_apples = self.k / new_potatoes
        
        # Apples received
        apples_received = self.apples - new_apples
        
        # Update pool state
        self.apples = new_apples
        self.potatoes = new_potatoes
        
        return apples_received
    
    def __str__(self):
        """
        Print the current state of the liquidity pool.
        """
        return f"Apples: {self.apples:.2f}, Potatoes: {self.potatoes:.2f}, k: {self.k:.2f}"

# Example Usage
if __name__ == "__main__":
    # Initialize pool with 100 apples and 100 potatoes
    amm = AMM(apples=100, potatoes=100)
    
    print("Initial Pool State:")
    print(amm)
    
    # Trade 10 apples for potatoes
    potatoes_received = amm.trade_apples_for_potatoes(10)
    print(f"\nTraded 10 apples for {potatoes_received:.2f} potatoes.")
    print("Pool State After Trade:")
    print(amm)
    
    # Trade 20 potatoes for apples
    apples_received = amm.trade_potatoes_for_apples(20)
    print(f"\nTraded 20 potatoes for {apples_received:.2f} apples.")
    print("Pool State After Trade:")
    print(amm)
