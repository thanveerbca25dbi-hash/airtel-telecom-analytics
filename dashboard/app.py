
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =====================================================
# 1. PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Airtel Telecom Analytics",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# 2. PROFESSIONAL DASHBOARD THEME
# =====================================================

st.markdown("""
<style>

/* Main background */
.stApp {
    background-color: #f5f7fb;
    color: #17243a;
}

/* Main title */
h1 {
    color: #e31e24 !important;
    font-size: 32px !important;
    font-weight: 800 !important;
}

h2, h3 {
    color: #17243a !important;
    font-weight: 700 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e5e8ef;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #ffffff;
    padding: 20px;
    border: 1px solid #e5e8ef;
    border-radius: 12px;
    box-shadow: 0 3px 12px rgba(20,35,60,0.04);
}

[data-testid="stMetricValue"] {
    color: #17243a;
    font-size: 28px;
    font-weight: 800;
}

[data-testid="stMetricLabel"] {
    color: #59677d;
    font-weight: 600;
}

/* Description banner */
.description {
    background: linear-gradient(90deg, #fff0f1, #ffffff);
    border-left: 5px solid #e31e24;
    padding: 16px 20px;
    border-radius: 9px;
    color: #29364b;
    margin-bottom: 20px;
}

/* Section headings */
.section-title {
    font-size: 19px;
    font-weight: 700;
    color: #17243a;
    margin-bottom: 12px;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
    border-bottom: 2px solid #e6e9f0;
}

.stTabs [data-baseweb="tab"] {
    height: 48px;
    background-color: #ffffff;
    border-radius: 8px 8px 0 0;
    padding: 10px 25px;
    font-weight: 700;
}

.stTabs [aria-selected="true"] {
    color: #e31e24 !important;
    border-bottom: 3px solid #e31e24 !important;
}

/* Chart containers */
div[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 12px;
}

/* Footer */
.footer {
    text-align: center;
    color: #7b8494;
    font-size: 12px;
    padding: 20px;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# 3. SAMPLE DATA
# =====================================================

monthly_data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Group A": [3.8, 3.8, 5.1, 4.8],
    "Group B": [4.3, 4.3, 5.1, 5.3],
    "Subscribers": [1.2, 1.5, 1.8, 2.0]
})

daily_data = pd.DataFrame({
    "Day": [
        "Mar 1", "Mar 4", "Mar 8", "Mar 11",
        "Mar 15", "Mar 18", "Mar 22", "Mar 25",
        "Mar 28", "Mar 30", "Mar 31"
    ],
    "Usage": [
        3.0, 3.5, 3.9, 3.3, 4.2,
        5.0, 4.6, 5.5, 4.7, 5.9, 6.2
    ]
})

allowance_data = pd.DataFrame({
    "Plan": ["Basic", "Standard", "Premium"],
    "Usage": [35, 30, 35]
})

device_data = pd.DataFrame({
    "Device": ["Mobile", "Tablet", "Others"],
    "Usage": [35, 30, 35]
})


# =====================================================
# 4. SIDEBAR
# =====================================================

with st.sidebar:

    st.divider()

    st.markdown("## ⚙️ Dashboard Filters")

    connection = st.selectbox(
        "Connection Type",
        ["All", "4G", "5G"]
    )

    experiment = st.selectbox(
        "Experiment Group",
        ["All", "Group A", "Group B"]
    )

    st.divider()

    st.markdown("### 📊 Dashboard Information")
    st.caption("Project: Airtel Telecom Analytics")
    st.caption("Category: Network Analytics")
    st.caption("Report Period: January – April 2025")

    st.divider()

    st.markdown(
        "<p style='color:#e31e24;font-weight:700;'>"
        "AIRTEL | CONNECTING INDIA</p>",
        unsafe_allow_html=True
    )


# =====================================================
# 5. MAIN HEADER
# =====================================================

st.title("Airtel Telecom Analytics")

st.markdown("""
<div class="description">
    <b>Network Performance & Capacity Planning</b><br>
    Monitor subscriber activity, data consumption,
    experiment performance and network demand.
</div>
""", unsafe_allow_html=True)


# =====================================================
# 6. CREATE TWO TABS
# =====================================================

overview_tab, detail_tab = st.tabs([
    "📊  Overview",
    "📈  Detail"
])


# =====================================================
# 7. OVERVIEW TAB
# =====================================================

with overview_tab:

    st.markdown("### Network Performance Overview")

    # KPI CARDS

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            label="📅 Usage-Days Count",
            value="1,200,000",
            help="Total validated usage days"
        )
        st.caption("Total validated usage days")

    with c2:
        st.metric(
            label="📊 T3 Test Result",
            value="p = 0.021 ↑"
        )
        st.caption("Significant increase")

    with c3:
        st.metric(
            label="👥 Data per Day",
            value="4.8 GB"
        )
        st.caption("Average per active day")

    st.write("")

    # MONTHLY DATA USAGE CHART

    left, right = st.columns([1.65, 1])

    with left:

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">'
                'Monthly Data Usage by Experiment Group'
                '</div>',
                unsafe_allow_html=True
            )

            fig = go.Figure()

            if experiment in ["All", "Group A"]:
                fig.add_trace(go.Bar(
                    x=monthly_data["Month"],
                    y=monthly_data["Group A"],
                    name="Group A",
                    marker_color="#1683e8"
                ))

            if experiment in ["All", "Group B"]:
                fig.add_trace(go.Bar(
                    x=monthly_data["Month"],
                    y=monthly_data["Group B"],
                    name="Group B",
                    marker_color="#e31e24"
                ))

            fig.update_layout(
                barmode="group",
                height=340,
                template="plotly_white",
                xaxis_title="Month",
                yaxis_title="Data Usage (GB)",
                yaxis=dict(range=[0, 6.5]),
                legend=dict(orientation="h", y=1.12),
                margin=dict(l=15, r=15, t=35, b=15)
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # SUBSCRIBER GROWTH

    with right:

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">'
                'Monthly Subscriber Count'
                '</div>',
                unsafe_allow_html=True
            )

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=monthly_data["Month"],
                y=monthly_data["Subscribers"],
                mode="lines+markers",
                line=dict(color="#1683e8", width=3),
                marker=dict(size=10),
                name="Subscribers"
            ))

            fig.update_layout(
                height=340,
                template="plotly_white",
                yaxis_title="Subscribers (Millions)",
                yaxis=dict(range=[0, 2.2]),
                showlegend=False,
                margin=dict(l=15, r=15, t=35, b=15)
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # ALLOWANCE UTILISATION

    st.write("")

    with st.container(border=True):

        st.markdown(
            '<div class="section-title">'
            'Allowance Utilisation by Plan'
            '</div>',
            unsafe_allow_html=True
        )

        fig = px.pie(
            allowance_data,
            names="Plan",
            values="Usage",
            hole=0.55,
            color="Plan",
            color_discrete_map={
                "Basic": "#1683e8",
                "Standard": "#e31e24",
                "Premium": "#20a44a"
            }
        )

        fig.update_traces(
            textinfo="percent",
            textposition="inside"
        )

        fig.update_layout(
            height=330,
            template="plotly_white",
            legend=dict(orientation="h"),
            margin=dict(l=15, r=15, t=15, b=15)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =====================================================
# 8. DETAIL TAB
# =====================================================

with detail_tab:

    st.markdown("### Detailed Network Analysis")

    st.markdown("""
    <div class="description">
        Explore detailed insights for a selected month.
    </div>
    """, unsafe_allow_html=True)

    # MONTH SELECTOR

    selected_month = st.selectbox(
        "📅 Select Reporting Month",
        [
            "January 2025",
            "February 2025",
            "March 2025",
            "April 2025"
        ],
        index=2
    )

    month_index = [
        "January 2025",
        "February 2025",
        "March 2025",
        "April 2025"
    ].index(selected_month)

    subscriber_value = monthly_data.iloc[
        month_index
    ]["Subscribers"]

    # DETAIL KPI CARDS

    c1, c2 = st.columns(2)

    with c1:
        st.metric(
            "👥 Active Subscribers",
            f"{subscriber_value:.1f}M"
        )
        st.caption("Selected month")

    with c2:
        st.metric(
            "🗄️ Data Carried",
            "8.6 PB"
        )
        st.caption("Selected month")

    st.write("")

    # DAILY TREND AND A/B COMPARISON

    left, right = st.columns([1.4, 1])

    with left:

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">'
                'Daily Data Load Trend'
                '</div>',
                unsafe_allow_html=True
            )

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=daily_data["Day"],
                y=daily_data["Usage"],
                mode="lines+markers",
                line=dict(color="#1683e8", width=3),
                marker=dict(size=8),
                fill="tozeroy",
                fillcolor="rgba(22,131,232,0.15)",
                name="Daily Usage"
            ))

            fig.update_layout(
                height=340,
                template="plotly_white",
                yaxis_title="Data Usage (GB)",
                yaxis=dict(range=[0, 7]),
                margin=dict(l=15, r=15, t=30, b=15)
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    with right:

        with st.container(border=True):

            st.markdown(
                '<div class="section-title">'
                'A/B Experiment Comparison'
                '</div>',
                unsafe_allow_html=True
            )

            comparison = pd.DataFrame({
                "Group": ["Group A", "Group B"],
                "Usage": [4.2, 5.1]
            })

            fig = px.bar(
                comparison,
                x="Group",
                y="Usage",
                color="Group",
                text="Usage",
                color_discrete_map={
                    "Group A": "#1683e8",
                    "Group B": "#e31e24"
                }
            )

            fig.update_layout(
                height=340,
                template="plotly_white",
                showlegend=False,
                yaxis_title="Data Usage (GB)",
                yaxis=dict(range=[0, 6.5]),
                margin=dict(l=15, r=15, t=30, b=15)
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

    # DEVICE COMPARISON

    st.write("")

    with st.container(border=True):

        st.markdown(
            '<div class="section-title">'
            'Device Usage Comparison'
            '</div>',
            unsafe_allow_html=True
        )

        fig = px.pie(
            device_data,
            names="Device",
            values="Usage",
            color="Device",
            color_discrete_map={
                "Mobile": "#1683e8",
                "Tablet": "#ff9f24",
                "Others": "#20a44a"
            }
        )

        fig.update_traces(
            textinfo="percent+label"
        )

        fig.update_layout(
            height=350,
            template="plotly_white",
            legend=dict(orientation="h"),
            margin=dict(l=15, r=15, t=15, b=15)
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


# =====================================================
# 9. FOOTER
# =====================================================

st.markdown("""
<div class="footer">
    Airtel Telecom Analytics |
    Network Performance & Capacity Planning |
    Dashboard Demo 2025
</div>
""", unsafe_allow_html=True)
