# Craig Lucas 
# Date: July 13, 2025
# Final Project : Enhanced employee pay calculator with:
# Input validation, statistical analysis, and readable summary table


import numpy
import statistics

# Define Employee class
class Employee:
    def __init__(self):
        self.name = ""
        self.hourly_rate = 0.0
        self.hours = []
        self.num_days = 0.0
        self.hours_mean = 0.0
        self.hours_median = 0.0
        self.hours_mode = 0.0
        self.hours_std = 0.0  # Addition Standard Deviation calculation
        self.hours_range = 0.0  # Addition Range calculation
        self.total_pay = 0.0

#  Addition 2: Input Validation method
#  Ensures users enter valid positives and handles errors

    def get_valid_float(self, prompt, min_value = 0.0 ):
        """Get a valid float input with minimum value validation"""
        while True:
            try:
                value = float(input(prompt))
                if value < min_value:
                    print(f"Please enter a number greater than or equal to{min_value}")
                    continue
                return value
            except ValueError:
                print("Please enter a valid number")


    def get_valid_int(self, prompt, min_value=1):
        """Get a valid integer input with minimum value validation"""
        while True:
            try:
                value = int(input(prompt))
                if value < min_value:
                    print(f"Please enter a number greater than or equal to {min_value}")
                    continue
                return value
            except ValueError:
                print("Please enter a valid whole number")

          
#  Enhanced User input with validation
    def get_input(self):
        print("=== Employee Pay Calculator ===\n")
        self.name = input("Enter your name:")
        self.hourly_rate = self.get_valid_float("Enter your hourly rate:$", 0.01)
        self.num_days = self.get_valid_int("How many days do you want to log hours for?", 1)
        for day in range(1, self.num_days + 1):
            daily_hours = self.get_valid_float(f"Enter hours worked for day {day}:",0.0)
            self.hours.append(daily_hours)

# Addition 1: Enhanced statistical calculation
# Adding in standard deviation and range calculations

    def calculate_averages(self):
        self.hours_mean = numpy.mean(self.hours)
        self.hours_median = numpy.median(self.hours)
        try:
            self.hours_mode = statistics.mode(self.hours)
        except statistics.StatisticsError:
            self.hours_mode = "No single mode"  #  When there is no Single mode
        
        # Calculate additional statistics
        self.hours_std = numpy.std(self.hours)
        self.hours_range = max(self.hours) - min(self.hours)


# Total pay calculation
    def calculate_total_pay(self):
        self.total_pay = sum(self.hours) * (self.hourly_rate)

# Addition 3: Table formatting for readability
    def print_pay_info(self):
        print("\n" + "="*50)
        print("Pay Summary Report")
        print("="*50)

#  Personalized message based on average hours
        if self.hours_mean > 8:
            print(f"You have been working over time, {self.name}! Enjoy some extra cash!")
        elif self.hours_mean >= 5:
            print(f"Thanks for logging your time, {self.name}.")
        else: 
            print(f"Did we schedule you enough hours, {self.name}?")        
        print("\n" + "="*50)
        print("Financial Details")
        print("-"*50)
        print(f"{'Total Hours Worked:':<25} {sum(self.hours):.2f} hours")
        print(f"{'Hourly Rate:':<25} ${self.hourly_rate:.2f}")
        print(f"{'TOTAL PAYCHECK:':<25} ${self.total_pay:.2f}")

        print("\n" + "-"*50)
        print("Work hour statistics")
        print("-"*50)

#  Create formatted statistics table

        stats_data = [
            ("Average (mean) hours per day", f"{self.hours_mean:.2f}"),
            ("Median hours worked per day", f"{self.hours_median:.2f}"),
            ("Most common (mode) hours worked", f"{self.hours_mode}"),
            ("Standard Deviation of hours", f"{self.hours_std:.2f}"),
            ("Range of hours worked", f"{self.hours_range:.2f}"),
            ("Minimum hours in a day", f"{min(self.hours):.2f}"),
            ("Maximum hours in a day", f"{max(self.hours):.2f}")
        ]

        for label, value in stats_data:
            print(f"{label:<35} {value:>12}")

        print("="*50)
        print("Thank you for using Pay Calculator!")
        print("="*50)    



# Main function
def main():
    print("Welcome to the Enhanced employee Pay Calculator!")
    print("This program will help you track your hours and calculate your total pay.\n")

    e = Employee()
    e.get_input()
    e.calculate_averages()
    e.calculate_total_pay()
    e.print_pay_info()

    print("\nProgram completed successfully!")

if __name__ == "__main__":
    main()



#  Final project additions summary

#  Addition 1: Advanced Statistics
#  Added standard deviation, range, min, and max hour tracking
#  Improved mode calculation with error handling
#  Why: Gives users a clearer picture of hour consistence and variation

#  Addition 2: Input Validation
#  Created methods to ensure positive, numeric input
#  Prevents negative or invalid entries for rate, days, and hours
#  Why: Ensures clean crash free input and user friendly experience

#  Addition 3: Clean, Professional Output
#  Formatted output into readable tables with clear sections
#  Rounded currency to 2 decimals, added visual formatting
#  Why: Makes the results easy to read and adds a polished look 

        



                                


    
        
                
