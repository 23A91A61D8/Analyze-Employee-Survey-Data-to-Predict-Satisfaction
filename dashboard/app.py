import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

# ---------------------------
# PROFESSIONAL CUSTOM CSS
# ---------------------------
st.markdown("""
<style>

/* ---- GOOGLE FONT ---- */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

/* ---- GLOBAL ---- */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main {
    background: linear-gradient(135deg, #0F1B2D 0%, #152238 50%, #0F1B2D 100%);
    min-height: 100vh;
}

/* ---- SIDEBAR ---- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0A1628 0%, #112040 100%);
    border-right: 1px solid #1E3A5F;
}
section[data-testid="stSidebar"] * {
    color: #CBD5E1 !important;
}
section[data-testid="stSidebar"] .stSelectbox label {
    color: #94A3B8 !important;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
}
section[data-testid="stSidebar"] h1 {
    color: #E2E8F0 !important;
    font-size: 1.1rem !important;
}

/* ---- MAIN TITLE ---- */
h1 {
    color: #F1F5F9 !important;
    font-size: 2rem !important;
    font-weight: 800 !important;
    letter-spacing: -0.02em;
}

/* ---- SECTION HEADERS ---- */
h2, h3 {
    color: #CBD5E1 !important;
    font-weight: 700 !important;
}

/* ---- METRIC CARDS ---- */
div[data-testid="metric-container"] {
    background: linear-gradient(135deg, #1E3A5F 0%, #1A3352 100%) !important;
    border: 1px solid #2D5080 !important;
    padding: 20px 24px !important;
    border-radius: 16px !important;
    box-shadow: 0 4px 24px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.05) !important;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
div[data-testid="metric-container"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.5), inset 0 1px 0 rgba(255,255,255,0.07) !important;
}
div[data-testid="metric-container"] label {
    color: #64B5F6 !important;
    font-size: 0.75rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.08em !important;
    text-transform: uppercase !important;
}
div[data-testid="metric-container"] [data-testid="stMetricValue"] {
    color: #F1F5F9 !important;
    font-size: 2rem !important;
    font-weight: 800 !important;
}

/* ---- PLOTLY CHART CONTAINERS ---- */
div[data-testid="stPlotlyChart"] {
    background: linear-gradient(135deg, #162030 0%, #1A2940 100%);
    border: 1px solid #243550;
    border-radius: 16px;
    padding: 8px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.35);
}

/* ---- DATAFRAME ---- */
div[data-testid="stDataFrame"] {
    background: #162030;
    border: 1px solid #243550;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.35);
}

/* ---- ALERTS & INFO ---- */
div[data-testid="stAlert"] {
    border-radius: 12px !important;
    border: none !important;
}

/* ---- DIVIDER ---- */
hr {
    border-color: #1E3A5F !important;
    margin: 24px 0 !important;
}

/* ---- SELECTBOX ---- */
div[data-baseweb="select"] > div {
    background-color: #1A2D47 !important;
    border-color: #2D5080 !important;
    border-radius: 10px !important;
    color: #E2E8F0 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------
# LOAD DATA
# ---------------------------
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "..", "data", "employee_satisfaction_processed.csv")
df = pd.read_csv(file_path)

# ---------------------------
# COLOUR PALETTE (shared)
# ---------------------------
PALETTE = {
    "blue":    "#3B82F6",
    "teal":    "#14B8A6",
    "purple":  "#A78BFA",
    "amber":   "#FBBF24",
    "rose":    "#F87171",
    "emerald": "#34D399",
    "sky":     "#38BDF8",
    "indigo":  "#818CF8",
}
CHART_BG   = "rgba(0,0,0,0)"
GRID_COLOR = "#1E3A5F"
FONT_COLOR = "#CBD5E1"

PLOTLY_LAYOUT = dict(
    paper_bgcolor=CHART_BG,
    plot_bgcolor=CHART_BG,
    font=dict(family="Inter", color=FONT_COLOR, size=12),
    title_font=dict(family="Inter", color="#F1F5F9", size=15, weight="bold"),
    legend=dict(
        bgcolor="rgba(15,27,45,0.6)",
        bordercolor="#2D5080",
        borderwidth=1,
        font=dict(color=FONT_COLOR)
    ),
    margin=dict(t=48, b=24, l=16, r=16),
    xaxis=dict(gridcolor=GRID_COLOR, zerolinecolor=GRID_COLOR, color=FONT_COLOR),
    yaxis=dict(gridcolor=GRID_COLOR, zerolinecolor=GRID_COLOR, color=FONT_COLOR),
)

def apply_layout(fig, title=""):
    fig.update_layout(**PLOTLY_LAYOUT, title_text=title)
    return fig

# ---------------------------
# TITLE
# ---------------------------
st.markdown("""
<div style="
    background: linear-gradient(135deg, #1E3A5F 0%, #0F2944 100%);
    border: 1px solid #2D5080;
    border-radius: 20px;
    padding: 28px 36px;
    margin-bottom: 28px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    text-align: center;
">
    <h1 style="margin:0; color:#F1F5F9; font-size:2.1rem;">
        📊 Employee Satisfaction &amp; Attrition Dashboard
    </h1>
    <p style="color:#64B5F6; margin:6px 0 0; font-size:0.92rem; font-weight:500; letter-spacing:0.04em;">
        REAL-TIME HR ANALYTICS · POWERED BY YOUR WORKFORCE DATA
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# SIDEBAR
# ---------------------------
st.sidebar.markdown("""
<div style="
    background: linear-gradient(135deg, #1E3A5F, #0F2944);
    border: 1px solid #2D5080;
    border-radius: 12px;
    padding: 14px 16px;
    margin-bottom: 16px;
    text-align: center;
">
    <span style="color:#38BDF8; font-size:1.4rem;">🔍</span>
    <p style="color:#F1F5F9; font-weight:700; margin:4px 0 0; font-size:1rem; letter-spacing:0.05em;">
        FILTERS
    </p>
</div>
""", unsafe_allow_html=True)

department = st.sidebar.selectbox(
    "Department",
    ["All"] + sorted(df["Department"].unique().tolist())
)

job_role = st.sidebar.selectbox(
    "Job Role",
    ["All"] + sorted(df["JobRole"].unique().tolist())
)

gender = st.sidebar.selectbox(
    "Gender",
    ["All"] + sorted(df["Gender"].unique().tolist())
)

# ---------------------------
# FILTER DATA
# ---------------------------
filtered_df = df.copy()
if department != "All":
    filtered_df = filtered_df[filtered_df["Department"] == department]
if job_role != "All":
    filtered_df = filtered_df[filtered_df["JobRole"] == job_role]
if gender != "All":
    filtered_df = filtered_df[filtered_df["Gender"] == gender]

if filtered_df.empty:
    st.error("⚠️ No records found for the selected filters. Please adjust your selection.")
    st.stop()

# ---------------------------
# KPIs
# ---------------------------
total_employees  = len(filtered_df)
attrition_rate   = round(filtered_df["Attrition"].eq("Yes").mean() * 100, 2)
avg_income       = round(filtered_df["MonthlyIncome"].mean(), 2)
avg_satisfaction = round(filtered_df["CompositeSatisfaction"].mean(), 2)

# coloured accent cards via HTML above each metric column
kpi_html = """
<div style="display:grid; grid-template-columns:repeat(4,1fr); gap:16px; margin-bottom:8px;">
  <div style="background:linear-gradient(135deg,#1E3A5F,#163055);border:1px solid #3B82F6;
       border-top:3px solid #3B82F6;border-radius:16px;padding:20px 20px 14px;
       box-shadow:0 4px 20px rgba(59,130,246,0.2);">
    <p style="color:#64B5F6;font-size:.72rem;font-weight:700;letter-spacing:.1em;
       text-transform:uppercase;margin:0 0 6px;">Total Employees</p>
    <p style="color:#F1F5F9;font-size:2rem;font-weight:800;margin:0;">{te}</p>
    <p style="color:#64B5F6;font-size:.72rem;margin:4px 0 0;">👥 Headcount</p>
  </div>
  <div style="background:linear-gradient(135deg,#3B1F1F,#2D1A1A);border:1px solid #F87171;
       border-top:3px solid #F87171;border-radius:16px;padding:20px 20px 14px;
       box-shadow:0 4px 20px rgba(248,113,113,0.2);">
    <p style="color:#FCA5A5;font-size:.72rem;font-weight:700;letter-spacing:.1em;
       text-transform:uppercase;margin:0 0 6px;">Attrition Rate</p>
    <p style="color:#F1F5F9;font-size:2rem;font-weight:800;margin:0;">{ar}%</p>
    <p style="color:#FCA5A5;font-size:.72rem;margin:4px 0 0;">📉 Turnover</p>
  </div>
  <div style="background:linear-gradient(135deg,#1A3024,#14281C);border:1px solid #34D399;
       border-top:3px solid #34D399;border-radius:16px;padding:20px 20px 14px;
       box-shadow:0 4px 20px rgba(52,211,153,0.2);">
    <p style="color:#6EE7B7;font-size:.72rem;font-weight:700;letter-spacing:.1em;
       text-transform:uppercase;margin:0 0 6px;">Avg Monthly Income</p>
    <p style="color:#F1F5F9;font-size:2rem;font-weight:800;margin:0;">₹{ai:,}</p>
    <p style="color:#6EE7B7;font-size:.72rem;margin:4px 0 0;">💰 Salary</p>
  </div>
  <div style="background:linear-gradient(135deg,#2D1F4A,#22183A);border:1px solid #A78BFA;
       border-top:3px solid #A78BFA;border-radius:16px;padding:20px 20px 14px;
       box-shadow:0 4px 20px rgba(167,139,250,0.2);">
    <p style="color:#C4B5FD;font-size:.72rem;font-weight:700;letter-spacing:.1em;
       text-transform:uppercase;margin:0 0 6px;">Avg Satisfaction</p>
    <p style="color:#F1F5F9;font-size:2rem;font-weight:800;margin:0;">{as_}</p>
    <p style="color:#C4B5FD;font-size:.72rem;margin:4px 0 0;">⭐ Score / 4</p>
  </div>
</div>
""".format(
    te=f"{total_employees:,}",
    ar=attrition_rate,
    ai=int(avg_income),
    as_=avg_satisfaction
)

st.markdown(kpi_html, unsafe_allow_html=True)
st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)

# ---------------------------
# ROW 1 — Attrition Donut | Department Bar
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    fig1 = go.Figure(go.Pie(
        labels=filtered_df["Attrition"].value_counts().index,
        values=filtered_df["Attrition"].value_counts().values,
        hole=0.6,
        marker=dict(
            colors=[PALETTE["emerald"], PALETTE["rose"]],
            line=dict(color="#0F1B2D", width=3)
        ),
        textinfo="label+percent",
        textfont=dict(color="#F1F5F9", size=13),
    ))
    fig1.update_layout(**PLOTLY_LAYOUT, title_text="🔄 Employee Attrition Split")
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    dept_count = (
        filtered_df.groupby("Department").size().reset_index(name="Employees")
    )
    colors = [PALETTE["blue"], PALETTE["teal"], PALETTE["purple"],
              PALETTE["amber"], PALETTE["sky"], PALETTE["indigo"]]
    fig2 = px.bar(
        dept_count, x="Department", y="Employees",
        color="Department",
        color_discrete_sequence=colors,
        text="Employees"
    )
    fig2.update_traces(
        textposition="outside",
        textfont=dict(color="#F1F5F9", size=12),
        marker_line_width=0,
    )
    apply_layout(fig2, "🏢 Employees by Department")
    st.plotly_chart(fig2, use_container_width=True)

# ---------------------------
# ROW 2 — Income vs Attrition Box | Job Satisfaction Histogram
# ---------------------------
col3, col4 = st.columns(2)

with col3:
    fig3 = px.box(
        filtered_df, x="Attrition", y="MonthlyIncome", color="Attrition",
        color_discrete_map={"Yes": PALETTE["rose"], "No": PALETTE["emerald"]},
        points="outliers"
    )
    fig3.update_traces(marker=dict(size=4, opacity=0.7))
    apply_layout(fig3, "💰 Monthly Income vs Attrition")
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    sat_palette = [PALETTE["sky"], PALETTE["blue"], PALETTE["purple"], PALETTE["indigo"]]
    fig4 = px.histogram(
        filtered_df, x="JobSatisfaction", color="JobSatisfaction",
        color_discrete_sequence=sat_palette,
        barmode="overlay",
        text_auto=True
    )
    fig4.update_traces(marker_line_width=0, opacity=0.85)
    apply_layout(fig4, "😊 Job Satisfaction Levels")
    st.plotly_chart(fig4, use_container_width=True)

# ---------------------------
# ROW 3 — Work-Life Balance | Age vs Income Scatter
# ---------------------------
col5, col6 = st.columns(2)

with col5:
    wlb_palette = [PALETTE["amber"], PALETTE["teal"], PALETTE["sky"], PALETTE["emerald"]]
    fig5 = px.histogram(
        filtered_df, x="WorkLifeBalance", color="WorkLifeBalance",
        color_discrete_sequence=wlb_palette,
        text_auto=True
    )
    fig5.update_traces(marker_line_width=0, opacity=0.85)
    apply_layout(fig5, "⚖️ Work-Life Balance Distribution")
    st.plotly_chart(fig5, use_container_width=True)

with col6:
    fig6 = px.scatter(
        filtered_df, x="Age", y="MonthlyIncome", color="Attrition",
        color_discrete_map={"Yes": PALETTE["rose"], "No": PALETTE["teal"]},
        opacity=0.75,
        hover_data=["JobRole", "Department"]
    )
    fig6.update_traces(marker=dict(size=7, line=dict(width=0.5, color="#0F1B2D")))
    apply_layout(fig6, "🎯 Age vs Monthly Income")
    st.plotly_chart(fig6, use_container_width=True)

# ---------------------------
# ATTRITION BY JOB ROLE — Horizontal Bar
# ---------------------------
st.markdown("<div style='height:4px'></div>", unsafe_allow_html=True)
st.markdown("""
<p style="color:#CBD5E1;font-size:1.05rem;font-weight:700;margin-bottom:8px;">
    📌 Attrition Rate by Job Role
</p>
""", unsafe_allow_html=True)

role_attr = (
    filtered_df.groupby("JobRole")["Attrition"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .reset_index(name="AttritionRate")
    .sort_values("AttritionRate", ascending=True)
)
fig_role = px.bar(
    role_attr, x="AttritionRate", y="JobRole",
    orientation="h",
    color="AttritionRate",
    color_continuous_scale=["#14B8A6", "#3B82F6", "#A78BFA", "#F87171"],
    text=role_attr["AttritionRate"].round(1).astype(str) + "%"
)
fig_role.update_traces(textposition="outside", textfont=dict(color="#F1F5F9"), marker_line_width=0)
fig_role.update_coloraxes(showscale=False)
apply_layout(fig_role, "")
st.plotly_chart(fig_role, use_container_width=True)

# ---------------------------
# CORRELATION MATRIX
# ---------------------------
st.markdown("""
<p style="color:#CBD5E1;font-size:1.05rem;font-weight:700;margin-bottom:8px;">
    📈 Feature Correlation Matrix
</p>
""", unsafe_allow_html=True)

numeric_df = filtered_df.select_dtypes(include="number")
corr = numeric_df.corr()

fig7 = px.imshow(
    corr, aspect="auto",
    color_continuous_scale=["#F87171", "#0F1B2D", "#3B82F6"],
    zmin=-1, zmax=1
)
apply_layout(fig7, "")
fig7.update_layout(
    coloraxis_colorbar=dict(
        title=dict(text="r", font=dict(color=FONT_COLOR)),
        tickfont=dict(color=FONT_COLOR),
    )
)
st.plotly_chart(fig7, use_container_width=True)

# ---------------------------
# HR INSIGHTS CARDS
# ---------------------------
highest_income_role = (
    filtered_df.groupby("JobRole")["MonthlyIncome"]
    .mean()
    .sort_values(ascending=False)
)

top_role   = highest_income_role.index[0] if len(highest_income_role) > 0 else "N/A"
top_salary = round(highest_income_role.iloc[0], 0) if len(highest_income_role) > 0 else 0

# Retention rate
retention = round(100 - attrition_rate, 2)

# Most common job role
top_jobrole_count = filtered_df["JobRole"].value_counts().idxmax()

st.markdown(f"""
<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:8px;">

  <div style="background:linear-gradient(135deg,#1A3024,#14281C);border:1px solid #34D399;
       border-radius:16px;padding:22px;box-shadow:0 4px 20px rgba(52,211,153,0.15);">
    <p style="color:#6EE7B7;font-size:.75rem;font-weight:700;letter-spacing:.1em;
       text-transform:uppercase;margin:0 0 8px;">🏆 Highest Paying Role</p>
    <p style="color:#F1F5F9;font-size:1.15rem;font-weight:700;margin:0 0 4px;">{top_role}</p>
    <p style="color:#34D399;font-size:1.4rem;font-weight:800;margin:0;">₹{int(top_salary):,} / mo</p>
  </div>

  <div style="background:linear-gradient(135deg,#1A3024,#14281C);border:1px solid #14B8A6;
       border-radius:16px;padding:22px;box-shadow:0 4px 20px rgba(20,184,166,0.15);">
    <p style="color:#5EEAD4;font-size:.75rem;font-weight:700;letter-spacing:.1em;
       text-transform:uppercase;margin:0 0 8px;">✅ Retention Rate</p>
    <p style="color:#F1F5F9;font-size:1.15rem;font-weight:700;margin:0 0 4px;">
       Employees staying on</p>
    <p style="color:#14B8A6;font-size:1.4rem;font-weight:800;margin:0;">{retention}%</p>
  </div>

  <div style="background:linear-gradient(135deg,#2D1F4A,#22183A);border:1px solid #A78BFA;
       border-radius:16px;padding:22px;box-shadow:0 4px 20px rgba(167,139,250,0.15);">
    <p style="color:#C4B5FD;font-size:.75rem;font-weight:700;letter-spacing:.1em;
       text-transform:uppercase;margin:0 0 8px;">👤 Most Common Role</p>
    <p style="color:#F1F5F9;font-size:1.15rem;font-weight:700;margin:0 0 4px;">{top_jobrole_count}</p>
    <p style="color:#A78BFA;font-size:.85rem;font-weight:600;margin:0;">
       {filtered_df["JobRole"].value_counts().iloc[0]} employees</p>
  </div>

</div>

<div style="background:linear-gradient(135deg,#1E3A5F,#162A4A);border:1px solid #2D5080;
     border-left:4px solid #3B82F6;border-radius:16px;padding:22px;margin-top:16px;
     box-shadow:0 4px 20px rgba(0,0,0,0.3);">
  <p style="color:#38BDF8;font-size:.8rem;font-weight:700;letter-spacing:.08em;
     text-transform:uppercase;margin:0 0 12px;">💡 Key Drivers of Employee Satisfaction</p>
  <div style="display:flex;flex-wrap:wrap;gap:10px;">
    <span style="background:#1A3352;border:1px solid #3B82F6;border-radius:8px;
         padding:6px 14px;color:#93C5FD;font-size:.82rem;font-weight:600;">
         ⚖️ Work-Life Balance</span>
    <span style="background:#1A3352;border:1px solid #14B8A6;border-radius:8px;
         padding:6px 14px;color:#5EEAD4;font-size:.82rem;font-weight:600;">
         😊 Job Satisfaction</span>
    <span style="background:#1A3352;border:1px solid #A78BFA;border-radius:8px;
         padding:6px 14px;color:#C4B5FD;font-size:.82rem;font-weight:600;">
         🌿 Environment Satisfaction</span>
    <span style="background:#1A3352;border:1px solid #FBBF24;border-radius:8px;
         padding:6px 14px;color:#FCD34D;font-size:.82rem;font-weight:600;">
         🤝 Relationship Satisfaction</span>
    <span style="background:#1A3352;border:1px solid #34D399;border-radius:8px;
         padding:6px 14px;color:#6EE7B7;font-size:.82rem;font-weight:600;">
         💰 Monthly Income</span>
  </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------
# DATA TABLE
# ---------------------------
st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
st.markdown("""
<p style="color:#CBD5E1;font-size:1.05rem;font-weight:700;margin-bottom:8px;">
    📄 Employee Dataset Preview
</p>
""", unsafe_allow_html=True)

st.dataframe(
    filtered_df.head(20),
    use_container_width=True,
    hide_index=True
)

# ---------------------------
# FOOTER
# ---------------------------
st.markdown("""
<div style="
    background:linear-gradient(135deg,#1E3A5F,#0F2944);
    border:1px solid #2D5080;
    border-radius:16px;
    padding:18px 28px;
    margin-top:24px;
    text-align:center;
    box-shadow:0 4px 20px rgba(0,0,0,0.3);
">
    <p style="color:#64B5F6;font-size:.85rem;font-weight:600;margin:0;">
        ✅ Dashboard Loaded Successfully &nbsp;·&nbsp; All filters are live &nbsp;·&nbsp;
        Data updates instantly on selection
    </p>
</div>
""", unsafe_allow_html=True)