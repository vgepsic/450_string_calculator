from calculate.operators import Operators

if __name__ == "__main__":
    print("Addition")
    user_input = input(f"Enter the expression to calculate : ")
    result = Operators.Add(user_input)
    print(f"RESULT : {user_input} = {result}")
