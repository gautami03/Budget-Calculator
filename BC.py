import streamlit as st

st.title("MONTHLY BUDGET TRACKER")
st.write("=" * 40)

# User Inputs
Monthly_Income = st.number_input("What is your monthly Income?", min_value=0, step=1)
Rent = st.number_input("What is your Rent?", min_value=0, step=1)
Food_Expenses = st.number_input("What is your Food Expenses?", min_value=0, step=1)
Transport_Expenses = st.number_input("What is your Transport Expenses?", min_value=0, step=1)

st.write("=" * 40)
st.write("=" * 40)

if st.button("Calculate Budget"):

    st.subheader("FINANCIAL SUMMARY")
    st.write("=" * 40)

    st.write("Monthly Income = ₹", Monthly_Income)

    Total_Expenses = Rent + Food_Expenses + Transport_Expenses
    st.write("Total Expenses = ₹", Total_Expenses)

    Total_Savings = Monthly_Income - Total_Expenses
    st.write("Total Savings = ₹", Total_Savings)

    st.write("=" * 40)

    if Monthly_Income > 0:
        st.write(
            "Your savings is",
            int(Total_Savings / Monthly_Income * 100),
            "% of your monthly income",
        )
        st.write(
            "Your expenses are",
            int(Total_Expenses / Monthly_Income * 100),
            "% of your monthly income",
        )
    else:
        st.write("Income is zero, percentage cannot be calculated.")

    st.write("=" * 40)
    st.subheader("RECOMMENDATION")
    st.write("=" * 40)

    # Savings analysis
    if Total_Savings > Monthly_Income * 0.5:
        st.success("YOU ARE SAVING WELL, NOW YOU SHOULD INVEST")
    elif Total_Savings > 0:
        st.warning("YOU ARE SAVING BUT YOU COULD SAVE MORE")
    elif Total_Savings == 0:
        st.info("YOU REALLY NEED TO SAVE MONEY")
    else:
        st.error("YOU ARE IN DEBT")

    # Expense analysis
    if Total_Expenses > Monthly_Income:
        st.error("YOU ARE SPENDING WAY TOO MUCH, YOU MAY GO IN DEBT")
    elif Total_Expenses > Monthly_Income * 0.5:
        st.warning("YOU ARE SPENDING MORE THAN 50% OF YOUR MONTHLY INCOME")
    elif Total_Expenses > Monthly_Income * 0.25:
        st.info("YOU ARE SPENDING AN ALRIGHT AMOUNT")
    elif Total_Expenses == 0:
        st.success("YOU ARE SPENDING NOTHING")
