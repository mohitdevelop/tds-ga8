import streamlit as st

def find_largest(a, b, c):
    return max(a, b, c)

def main():
    st.title("Greatest Number")
    
    st.write("Enter three numbers below:")
    
    num1 = st.number_input("Enter first number", value=0)
    num2 = st.number_input("Enter second number", value=0)
    num3 = st.number_input("Enter third number", value=0)
    
    if st.button("Find Largest"):
        largest = find_largest(num1, num2, num3)
        st.write(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
