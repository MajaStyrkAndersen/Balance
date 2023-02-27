from itu.algs4.fundamentals.stack import Stack
from itu.algs4.stdlib.stdio import readString

# Implement stack data type, where push and pop operations can be perfomed (LIFO-principle)

# Output is 1 if input is balanced e.g. [(())]
# Output is 0 if input is not balanced e.g. ([)]

def main():
    input = readString()
    st = Stack()

    for bracket in input:
        if bracket == "(" or bracket == "[":
            st.push(bracket)

        if bracket == ")" or bracket == "]":
            if not st.is_empty():

                if st.peek() == "(" or bracket == "]":
                    st.pop()
            
            else:
                return print(0)

    if not st.is_empty():
        return print(0)

    return print(1)

if __name__ == "__main__":
    main()