# streamlit run streamlit_app/linking_app.py
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_extras import colored_header
from streamlit_extras.grid import grid 

# Predefined settings
st.set_page_config(layout="wide")

st.markdown("""
<style>
.big-font {
    font-size:30px !important;
}
</style>
""", unsafe_allow_html=True)

# Reading data
cr = pd.read_csv('streamlit_app/cr.csv')
cr.set_index('type', inplace=True)
long_cr = pd.read_csv('streamlit_app/long_cr.csv')

all_cr = pd.read_csv('streamlit_app/all_cr.csv')
all_cr.set_index('type', inplace=True)
long_all_cr = pd.read_csv('streamlit_app/long_all_cr.csv')

cr_lt = pd.read_csv('streamlit_app/cr_lt.csv')
cr_lt.set_index('type', inplace=True)
long_cr_lt = pd.read_csv('streamlit_app/long_cr_lt.csv')

rt_table = pd.read_csv('streamlit_app/rt_table.csv')
rt_table_new = rt_table.copy()
rt_table_new.set_index('lt', inplace=True)

rt_table_year_month = pd.read_csv('streamlit_app/rt_table_year_month.csv')
rt_table_year_month_new = rt_table_year_month.copy().sort_values(by = ['year_month', 'lt'])
rt_table_year_month_new.set_index('lt', inplace=True)

st.markdown(" # Cosmetic Analytics 💅")
st.write('Use Navigation Bar to view other pages')

# Line divider
st.markdown('<hr>', unsafe_allow_html=True)

# App tree
def welcome_page():
    st.markdown('''
    ## [Data set](https://www.kaggle.com/datasets/mkechinov/ecommerce-events-history-in-cosmetics-shop)
    <p class="big-font"> 1. Dataset contains behavior information for 5 months (Oct 2019 – Feb 2020) from a medium cosmetics online store </p>
    <p class="big-font"> 2. Each row in the file represents an event </p>
    <p class="big-font"> 3. All events are related to products and users </p>
    <p class="big-font"> 4. Each event is like many-to-many relation between products and user </p>
    ''', unsafe_allow_html=True)

    st.markdown(''' ''')
    st.markdown(''' ''')
    st.markdown(''' ''')
    st.markdown(''' ''')

    st.markdown('''
    ## Main Task
    <p class="big-font"> 1. Let's pretend that the owner of a cosmetic website came to us and asked us to make a performance assessment of his product </p>
    <p class="big-font"> 2. We should pick several metrics to evaluate his website and give recommendations on what steps should be taken in the future </p>
    <p class="big-font"> 3. Every question is related to a concrete KPI </p>
    <p class="big-font"> 4. The recommendations should be general and include a 'call to action' </p>
    ''', unsafe_allow_html=True)

    st.markdown(''' ''')
    st.markdown(''' ''')
    st.markdown(''' ''')
    st.markdown(''' ''')

    st.markdown('''
    ## List of questions
    **<p class="big-font"> Conversion Rate: </p>**
    <p class="big-font"> 1. What is the overall conversion rate ? </p>
    <p class="big-font"> 2. Which year / month have the highest CR ? </p>
    <p class="big-font"> 3. Which funnel steps should be improved ? </p>
    <br> 
                    
    **<p class="big-font"> Retention: </p>**
    <p class="big-font"> 1. What is the retention of the product ? </p>
    <p class="big-font"> 2. Do the RT values differ across different years and months ? </p>
    <p class="big-font"> 3. Are the RT values stable or not ? </p>
    ''', unsafe_allow_html=True)


# Overall CR page
def overall_cr():

    # Header & description
    st.markdown(''' 
    ## Overall CR
    <p class="big-font"> We start our analysis with overall conversion rates: table with CR values and its graphical representationr</p>
    ''', unsafe_allow_html=True)
    st.write(''' ''')

    # First grid - table & graph
    my_grid_overall_cr = grid(2, 1, vertical_align="center", gap = 'large')

    # Table
    my_grid_overall_cr.dataframe(cr, width = 1300)

    # Graph
    my_grid_overall_cr.bar_chart(long_cr, 
                    x='variable', 
                    y='value', 
                    color='type', 
                    use_container_width=True,
                    height = 600) 

    # Line divider
    st.markdown('<hr>', unsafe_allow_html=True)

    # Second grind for text
    second_grid_overall_cr = grid(2, 1, vertical_align="top", gap = 'large')

    # Interpretation
    second_grid_overall_cr.markdown('''
    ## Interpretation
    <p class="big-font"> 1. The problematic stage is purchase </p>
    <p class="big-font"> 2. Few people add items to the cart (25%), but even fewer buy them (28%) </p>
    <p class="big-font"> 3. Actions: more than a half of it belong to cart (59%)</p>
    <p class="big-font"> 4. Practically, every sixth action is related to purchase (15%)</p>
    ''', unsafe_allow_html=True)

    # Description
    second_grid_overall_cr.markdown('''
    ## Description
    <p class="big-font"> 1. Graphs above illustrate funnel steps </p>
    <p class="big-font"> 2. User's flow: view product -> add item to the cart -> purchase item </p>
    <p class="big-font"> 3. First two CR are relative (% from view product to add item to cart) </p>
    <p class="big-font"> 4. There's one absolute CR (% from view product to purchase) </p>
    ''', unsafe_allow_html=True)

# CR by year / month
def cr_year_month():
    
    # Title & description
    st.markdown(''' 
    ## CR – year & month
    <p class="big-font"> Next, we will take a look at CR values by year & month for users / actions separately</p>
    ''', unsafe_allow_html=True)
    st.write(''' ''')

    st.dataframe(all_cr, width = 3000)
    st.write(''' ''')
    grid_headers = grid(2, 1, vertical_align="center", gap = 'large')

    grid_headers.markdown('## Users', unsafe_allow_html=True)
    grid_headers.markdown('## Actions', unsafe_allow_html=True)

    my_grid_cr_year_month = grid(2, 2, vertical_align="center", gap = 'large')


    my_grid_cr_year_month.bar_chart(long_all_cr.query('type == "users"'), 
                    x='year_month', 
                    y='value', 
                    color='variable', 
                    use_container_width=True,
                    height = 600) 
    
    my_grid_cr_year_month.bar_chart(long_all_cr.query('type == "actions"'), 
                    x='year_month', 
                    y='value', 
                    color='variable', 
                    use_container_width=True,
                    height = 600) 

    # Line divider
    st.markdown('<hr>', unsafe_allow_html=True)

    # Interpretation
    st.markdown('''
    ## Interpretation
    <p class="big-font"> 1. There's no significant difference between groups </p>
    <p class="big-font"> 2. Except for 2019-10: CR from cart to purch is the lowest (users) </p>
    <p class="big-font"> 3. Probably, the seasonal factor does not affect on users </p>
    ''', unsafe_allow_html=True)

# CR by lt
def cr_lt_f():
    
    # Title & description
    st.markdown(''' 
    ## CR – 2020-Jan & LT >= 14
    <p class="big-font"> Finally, we want to look at specific sample: users who 'lived' more than 14 days in January 2020</p>
    ''', unsafe_allow_html=True)
    st.write(''' ''')

    # Starting grid
    my_grid_cr_lt = grid(2, 1, vertical_align="center", gap = 'large')

    # Table 
    my_grid_cr_lt.dataframe(cr_lt, width = 3000)

    # Graph
    my_grid_cr_lt.bar_chart(long_cr_lt, 
                    x='variable', 
                    y='value', 
                    color='type', 
                    use_container_width=True,
                    height = 600) 

    # Line divider
    st.markdown('<hr>', unsafe_allow_html=True)

    # Interpretation
    st.markdown('''
    ## Interpretation
    <p class="big-font"> 1. The CR values (by users) have increased compared to the results for the whole group </p>
    <p class="big-font"> 2. Practically, every 2d user makes at least one transaction after cart (60% CR cart -> purchase)</p>
    <p class="big-font"> 3. Every 5th action after cart corresponds to a purchase (22% CR cart -> purchase) </p>
    <p class="big-font"> 4. Every 4th user, after viewing an item, will buy it (27% CR view -> purchase) </p>
    <p class="big-font"> 5. Every 10th action after viewing an item corresponds to a purchase (13% CR view -> purchase) </p>
    ''', unsafe_allow_html=True)


# Retention
def retention_f():
    # Title & description
    st.markdown(''' 
    ## Retention Analysis
    <p class="big-font"> We think that the main problem is related to retention, so let's take a look at it</p>
    ''', unsafe_allow_html=True)
    st.write(''' ''')

    # Heading for first grid
    st.markdown('## Overall RT', unsafe_allow_html=True)
    
    # Starting grid
    my_grid_retention = grid(2, 1, vertical_align="top", gap = 'large')

    # Heading for second grid
    st.markdown('## RT by year & month', unsafe_allow_html=True)

    # Table 1 – RT Overall
    my_grid_retention.dataframe(rt_table_new, width = 3000, height = 520)

    # Graph 1 – RT Overall
    my_grid_retention.line_chart(rt_table, 
                                    x='lt', 
                                    y='rt', 
                                    use_container_width=True,
                                    height = 600) 
    
    # Second grid
    my_grid_retention_second = grid(2, 1, vertical_align="top", gap = 'large')

    # Table 2 – RT by year & month
    my_grid_retention_second.dataframe(rt_table_year_month_new, width = 3000, height = 520)

    # Graph 2 – RT by year & month
    my_grid_retention_second.bar_chart(rt_table_year_month, 
                    x='lt', 
                    y='rt', 
                    color='year_month', 
                    use_container_width=True,
                    height = 600) 

    # Line divider
    st.markdown('<hr>', unsafe_allow_html=True)

    # Third grind for text
    my_grid_retention_third = grid(2, 1, vertical_align="top", gap = 'large')

    # Interpretation – Overall RT
    my_grid_retention_third.markdown('''
    ## Interpretation – Overall RT
    <p class="big-font"> 1. It is incorrect to calculate RT by view actions, since it is not the first action </p>
    <p class="big-font"> 2. We see that trend continue to decrease: we don't observe the plateau</p>
    ''', unsafe_allow_html=True)

    # Interpretation – RT by year & month
    my_grid_retention_third.markdown('''
    ## Interpretation – RT by year & month
    <p class="big-font"> 1. In November 2019 – users 'visited' website more often, than the other dates </p>
    <p class="big-font"> 2. We don't observe the plateau for each month-year </p>
    <p class="big-font"> 3. The website should probably focus on increasing Retention </p>
    ''', unsafe_allow_html=True)

    # Line divider
    st.markdown('<hr>', unsafe_allow_html=True)

    # Fourth grind for text
    my_grid_retention_fourth = grid(2, 1, vertical_align="top", gap = 'large')

    my_grid_retention_fourth.markdown('''
    ## Conclusion
    <p class="big-font"> 1. The overall CR values are low: only 7% of users make a purchase after viewing </p>
    <p class="big-font"> 2. The results do not change if we look through particular years & months </p>
    <p class="big-font"> 3. Therefore, we selected a sample who was active >= 14 days in Jan 2020 </p>
    <p class="big-font"> 4. The results of this group were higher compared to the whole sample </p>
    <p class="big-font"> 5. Consequently, we proposed that the main problem is related to retention </p>
    <p class="big-font"> 6. In RT analysis we discovered that the product does not retain users well (there's no plateau) </p>
    ''', unsafe_allow_html=True)

                                                                                      
    my_grid_retention_fourth.markdown('''
    ## Recommendations
    <p class="big-font"> If the main problem is related to retention – the product should consider using: </p>
    <p class="big-font"> 1. push notifications </p>
    <p class="big-font"> 2. re-targeting campaigns </p>
    <p class="big-font"> 3. discounts & special offer days  </p>

    ''', unsafe_allow_html=True)

def main():
    st.sidebar.title('Navigation')
    pages = {
        'Project': welcome_page,
        'Overall CR': overall_cr,
        'CR by year & month': cr_year_month,
        'CR LT >= 14 & 2020-Jan': cr_lt_f,
        'Retention analysis': retention_f
    }

    # Project page as current page
    if 'current_page' not in st.session_state:
        st.session_state.current_page = 'Project'

    # Update links on navigation bar
    for name in pages:
        if st.sidebar.button(name):
            st.session_state.current_page = name

    # Call the appropriate page function
    pages[st.session_state.current_page]()

if __name__ == "__main__":
    main()