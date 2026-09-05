import streamlit as st
import pandas as pd
import random

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="MerchantAI Dashboard",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("🛍️ MerchantAI")
st.caption("AI-Powered Merchant Revenue Growth Dashboard")

st.success("🟢 System Online")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("MerchantAI")

page = st.sidebar.radio(
    "Navigation",
    [
        "📊 Dashboard",
        "🤖 AI Sales Agent",
        "🛒 Checkout",
        "📦 Products",
        "🧾 Transactions",
        "🔍 Audit Trail"
    ]
)

# ==================================================
# DASHBOARD
# ==================================================

if page == "📊 Dashboard":

    st.header("📊 Merchant Dashboard")

    # --------------------------------------------------
    # SAMPLE METRICS
    # --------------------------------------------------

    revenue = 24580
    orders = 48
    conversion = 12.4
    ai_growth = 18.6

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "💰 Total Revenue",
            f"₹{revenue:,}",
            "+12.5%"
        )

    with col2:
        st.metric(
            "🛒 Orders",
            orders,
            "+8"
        )

    with col3:
        st.metric(
            "📈 Conversion Rate",
            f"{conversion}%",
            "+2.1%"
        )

    with col4:
        st.metric(
            "🤖 AI Revenue Growth",
            f"{ai_growth}%",
            "+5.4%"
        )

    st.divider()

    # --------------------------------------------------
    # REVENUE CHART
    # --------------------------------------------------

    st.subheader("📈 Revenue Analytics")

    chart_data = pd.DataFrame({
        "Revenue": [
            2100,
            3200,
            2800,
            4500,
            3900,
            5200,
            2880
        ]
    })

    chart_data.index = [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun"
    ]

    st.line_chart(chart_data)

    st.divider()

    # --------------------------------------------------
    # TOP PRODUCTS
    # --------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🔥 Top Products")

        products = pd.DataFrame({
            "Product": [
                "AeroRun Running Shoes",
                "PulseFit Smart Watch",
                "SoundMax Earbuds",
                "TrailPro Backpack"
            ],
            "Sales": [
                18,
                12,
                10,
                8
            ],
            "Revenue": [
                "₹53,982",
                "₹53,988",
                "₹19,990",
                "₹12,792"
            ]
        })

        st.dataframe(
            products,
            use_container_width=True,
            hide_index=True
        )

    # --------------------------------------------------
    # AI INSIGHTS
    # --------------------------------------------------

    with col2:

        st.subheader("🤖 AI Insights")

        st.info(
            "💡 Customers purchasing running shoes "
            "have a high probability of buying sports "
            "backpacks."
        )

        st.success(
            "🚀 AI recommends a 10% bundle offer "
            "for Shoes + Backpack."
        )

        st.warning(
            "⚠️ PulseFit Smart Watch stock is getting low."
        )

        st.write(
            "🎯 Suggested action: Create a personalized "
            "cross-sell campaign."
        )

    st.divider()

    # --------------------------------------------------
    # RECENT TRANSACTIONS
    # --------------------------------------------------

    st.subheader("🧾 Recent Transactions")

    transactions = pd.DataFrame({
        "Order ID": [
            "#ORD001",
            "#ORD002",
            "#ORD003",
            "#ORD004",
            "#ORD005"
        ],
        "Product": [
            "AeroRun Running Shoes",
            "SoundMax Earbuds",
            "PulseFit Smart Watch",
            "TrailPro Backpack",
            "AeroRun Running Shoes"
        ],
        "Amount": [
            "₹2999",
            "₹1999",
            "₹4499",
            "₹1599",
            "₹2999"
        ],
        "Status": [
            "✅ Paid",
            "✅ Paid",
            "✅ Paid",
            "⏳ Pending",
            "✅ Paid"
        ]
    })

    st.dataframe(
        transactions,
        use_container_width=True,
        hide_index=True
    )


# ==================================================
# AI SALES AGENT
# ==================================================

elif page == "🤖 AI Sales Agent":

    st.header("🤖 AI Sales Agent")

    st.write(
        "Ask MerchantAI to recommend products, "
        "upsell customers or create a checkout proposal."
    )

    user_message = st.text_input(
        "What does the customer want?"
    )

    if st.button("🚀 Ask AI Agent"):

        if user_message:

            st.success(
                "AI Agent Recommendation"
            )

            st.write(
                "Based on the customer's requirement, "
                "MerchantAI recommends AeroRun Running Shoes."
            )

            st.info(
                "💡 Upsell opportunity: "
                "TrailPro Sports Backpack"
            )

        else:

            st.warning("Please enter a customer request.")


# ==================================================
# CHECKOUT
# ==================================================

elif page == "🛒 Checkout":

    st.header("🛒 AI Checkout")

    product = st.selectbox(
        "Select Product",
        [
            "AeroRun Running Shoes",
            "PulseFit Smart Watch",
            "SoundMax Earbuds",
            "TrailPro Sports Backpack"
        ]
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=1
    )

    price = {
        "AeroRun Running Shoes": 2999,
        "PulseFit Smart Watch": 4499,
        "SoundMax Earbuds": 1999,
        "TrailPro Sports Backpack": 1599
    }

    total = price[product] * quantity

    st.metric(
        "Total Amount",
        f"₹{total}"
    )

    approved = st.checkbox(
        "I approve this transaction"
    )

    if st.button("💳 Create Payment"):

        if approved:

            st.success(
                "✅ Payment request approved!"
            )

            st.info(
                "Razorpay Test Mode payment link "
                "will be generated here."
            )

        else:

            st.error(
                "Transaction requires explicit approval."
            )


# ==================================================
# PRODUCTS
# ==================================================

elif page == "📦 Products":

    st.header("📦 Product Catalog")

    products = pd.DataFrame({
        "Product": [
            "AeroRun Running Shoes",
            "PulseFit Smart Watch",
            "SoundMax Wireless Earbuds",
            "TrailPro Sports Backpack",
            "ClickPro Wireless Mouse"
        ],
        "Price": [
            "₹2999",
            "₹4499",
            "₹1999",
            "₹1599",
            "₹799"
        ],
        "Stock": [
            42,
            18,
            65,
            30,
            55
        ]
    })

    st.dataframe(
        products,
        use_container_width=True,
        hide_index=True
    )


# ==================================================
# TRANSACTIONS
# ==================================================

elif page == "🧾 Transactions":

    st.header("🧾 Transactions")

    transactions = pd.DataFrame({
        "Order ID": [
            "ORD001",
            "ORD002",
            "ORD003",
            "ORD004"
        ],
        "Amount": [
            "₹2999",
            "₹1999",
            "₹4499",
            "₹1599"
        ],
        "Status": [
            "Paid",
            "Paid",
            "Paid",
            "Pending"
        ]
    })

    st.dataframe(
        transactions,
        use_container_width=True,
        hide_index=True
    )


# ==================================================
# AUDIT TRAIL
# ==================================================

elif page == "🔍 Audit Trail":

    st.header("🔍 AI Audit Trail")

    st.write(
        "Every important AI and payment action "
        "is recorded for transparency."
    )

    audit = pd.DataFrame({
        "Time": [
            "19:30",
            "19:32",
            "19:34",
            "19:36"
        ],
        "Action": [
            "AI Recommendation",
            "Upsell Suggested",
            "Checkout Approved",
            "Payment Link Created"
        ],
        "Status": [
            "✅",
            "✅",
            "✅",
            "✅"
        ]
    })

    st.dataframe(
        audit,
        use_container_width=True,
        hide_index=True
    )