import streamlit as st
import pickle
import numpy as np
import sklearn
from streamlit_option_menu import option_menu
from PIL import Image


# Functionsstrea
def predict_status(ctry,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,slgplg,itmdt,itmmn,itmyr,deldtdy,deldtmn,deldtyr):

    #change the datatypes "string" to "int"
    itdd= int(itmdt)
    itdm= int(itmmn)
    itdy= int(itmyr)

    dydd= int(deldtdy)
    dydm= int(deldtmn)
    dydy= int(deldtyr)
    #modelfile of the classification
    with open(r"C:\Users\ramya\Classification_model.pkl","rb") as f:
        model_class=pickle.load(f)

    user_data= np.array([[ctry,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,
                       slgplg,itdd,itdm,itdy,dydd,dydm,dydy]])
    
    y_pred= model_class.predict(user_data)

    if y_pred == 1:
        return 1
    else:
        return 0

def predict_selling_price(ctry,sts,itmtp,aplcn,wth,prdrf,qtlg,cstlg,
                   tknslg,itmdt,itmmn,itmyr,deldtdy,deldtmn,deldtyr):

    #change the datatypes "string" to "int"
    itdd= int(itmdt)
    itdm= int(itmmn)
    itdy= int(itmyr)

    dydd= int(deldtdy)
    dydm= int(deldtmn)
    dydy= int(deldtyr)
    #modelfile of the classification
    with open(r"C:\Users\ramya\Regression_Model.pkl","rb") as f:
        model_regg=pickle.load(f)

    user_data= np.array([[ctry,sts,itmtp,aplcn,wth,prdrf,qtlg,cstlg,tknslg,
                       itdd,itdm,itdy,dydd,dydm,dydy]])
    
    y_pred= model_regg.predict(user_data)

    ac_y_pred= np.exp(y_pred[0])

    return ac_y_pred


st.set_page_config(layout= "wide")

st.title(":red[INDUSTRIAL COPPER MODELING]")

with st.sidebar:
    option = option_menu('Main Menu', options=["Home","Price Prediction", "Status Prediction","Conclusion"])

if option == "Home":
    st.write('''Welcome to "Industrial Copper Modeling" Application! This platform is designed to address the challenges faced by the copper industry  
             in making accurate sales and price predictions.''')
    col1, col2 = st.columns(2)
    with col1:
        st.header(":red[Key Challenges]")
        st.subheader("1.Skewed and Noisy Data")
        st.write("Sales and pricing data can be heavily skewed and noisy, making manual predictions less reliable. ")
        st.subheader("2.Optimal Pricing Decisions")
        st.write("Ensuring accurate pricing decisions in the presence of skewed data and outliers.")
        st.subheader("3.Lead Classification")
        st.write("Evaluating and Lead classifying leads to determine the likelihood of converting them into customers.")
    with col2 :
        st.image(Image.open(r"C:\Users\ramya\Copper_image2.jpeg"),width= 500)
    st.header(":red[Solution]")
    st.header("1. Data exploration and Preprocessing")
    st.subheader("Skewness and Outliers:")
    st.write(" Explore and address skewness and outliers in the dataset.")
    st.subheader("Data Cleaning and Transformation:")
    st.write("Transform the data into a suitable format and perform necessary cleaning and preprocessing steps.")
    st.header("2. Machine Learning Models")
    st.subheader("Regression Model:")
    st.write("Predict the continuous variable Selling_Price using a robust regression model.")
    st.subheader("Classification Model:")
    st.write("Predict the lead Status (WON or LOST) to help capture potential leads effectively.")
    st.header(":red[Features]")
    st.subheader("Selling Price Prediction:")
    st.write("Enter the relevant data for various features, and our regression model will predict the selling price accurately.")
    st.subheader("Lead Status Prediction:")
    st.write("Input the necessary details, and our classification model will predict whether the lead status is WON or LOST, helping you prioritize leads better.")

if option == "Status Prediction":

    st.header("Status Prediction (Won / Lost)")
    st.write(" ")

    col1,col2= st.columns(2)

    with col1:
        country= st.number_input(label="**Enter the Value for COUNTRY** / Min:25.0, Max:113.0")
        item_type= st.number_input(label="**Enter the Value for ITEM TYPE**/ Min:0.0, Max:6.0")
        application= st.number_input(label="**Enter the Value for APPLICATION**/ Min:2.0, Max:87.5")
        width= st.number_input(label="**Enter the Value for WIDTH**/ Min:700.0, Max:1980.0")
        product_ref= st.number_input(label="**Enter the Value for PRODUCT REF**/ Min:611728, Max:1722207579")
        quantity_tons_log= st.number_input(label="**Enter the Value for QUANTITY TONS(Log Value)**/ Min:-0.322, Max:6.924",format="%0.15f")
        customer_log= st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**/ Min:17.21910, Max:17.23015",format="%0.15f")
        thickness_log= st.number_input(label="**Enter the Value for THICKNESS (Log Value)**/ Min:-1.71479, Max:3.28154",format="%0.15f")
    
    with col2:
        selling_price_log= st.number_input(label="**Enter the Value for SELLING PRICE (Log Value)**/ Min:5.97503, Max:7.39036",format="%0.15f")
        item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
        delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))
        

    button= st.button("**PREDICT THE STATUS**",use_container_width=True)

    if button:
        status= predict_status(country,item_type,application,width,product_ref,quantity_tons_log,
                               customer_log,thickness_log,selling_price_log,item_date_day,
                               item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                               delivery_date_year)
        
        if status == 1:
            st.write("## :green[**The Status is Won !**]")
        else:
            st.write("## :red[**The Status is Lost !**]")

if option == "Price Prediction":

    st.header("**Selling Price Prediction**")
    st.write(" ")

    col1,col2= st.columns(2)

    with col1:
        country= st.number_input(label="**Enter the Value for COUNTRY**/ Min:25.0, Max:113.0")
        status= st.number_input(label="**Enter the Value for STATUS**/ Min:0.0, Max:8.0")
        item_type= st.number_input(label="**Enter the Value for ITEM TYPE**/ Min:0.0, Max:6.0")
        application= st.number_input(label="**Enter the Value for APPLICATION**/ Min:2.0, Max:87.5")
        width= st.number_input(label="**Enter the Value for WIDTH**/ Min:700.0, Max:1980.0")
        product_ref= st.number_input(label="**Enter the Value for PRODUCT REF**/ Min:611728, Max:1722207579")
        quantity_tons_log= st.number_input(label="**Enter the Value for QUANTITY TONS (Log Value)**/ Min:-0.3223343801166147, Max:6.924734324081348",format="%0.15f")
        customer_log= st.number_input(label="**Enter the Value for CUSTOMER (Log Value)**/ Min:17.21910565821408, Max:17.230155364880137",format="%0.15f")
        
    
    with col2:
        thickness_log= st.number_input(label="**Enter the Value for THICKNESS (Log Value)**/ Min:-1.7147984280919266, Max:3.281543137578373",format="%0.15f")
        item_date_day= st.selectbox("**Select the Day for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        item_date_month= st.selectbox("**Select the Month for ITEM DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        item_date_year= st.selectbox("**Select the Year for ITEM DATE**",("2020","2021"))
        delivery_date_day= st.selectbox("**Select the Day for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"))
        delivery_date_month= st.selectbox("**Select the Month for DELIVERY DATE**",("1","2","3","4","5","6","7","8","9","10","11","12"))
        delivery_date_year= st.selectbox("**Select the Year for DELIVERY DATE**",("2020","2021","2022"))
        

    button= st.button("**PREDICT THE SELLING PRICE**",use_container_width=True)

    if button:
        price= predict_selling_price(country,status,item_type,application,width,product_ref,quantity_tons_log,
                               customer_log,thickness_log,item_date_day,
                               item_date_month,item_date_year,delivery_date_day,delivery_date_month,
                               delivery_date_year)
        
        
        st.write("## :green[The Selling Price is :]",price)

if option == "Conclusion":

    st.header(":red[Conclusion]")
    st.write('''This Industrial Copper Modeling project offers a comprehensive learning experience, touching on various aspects of data analysis,
          machine learning, and web application development. Here are the key learning outcomes:''')
    st.header(":red[Learning Outcomes]")
    st.subheader("1.Proficiency in Python and Data Analysis Libraries:")
    st.write("Develop strong skills in Python programming.")
    st.write("Gain expertise in using data analysis libraries such as Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, and Streamlit.")
    st.subheader("2.Data Preprocessing Techniques:")
    st.write("Learn to handle missing values, detect outliers, and normalize data to prepare it for machine learning models.")
    st.write("Master essential data preprocessing techniques to ensure data quality and reliability.")
    st.subheader("3.Exploratory Data Analysis (EDA):")
    st.write("Understand and visualize data using EDA techniques such as boxplots, histograms, and scatter plots.")
    st.write("Gain insights into data distribution and relationships between variables.")
    st.subheader("4.Advanced Machine Learning Techniques:")
    st.write("Learn and apply regression models to predict continuous variables, specifically the Selling Price.")
    st.write("Implement classification models to predict binary target variables, such as lead Status (WON or LOST).")
    st.subheader("5.Model Building and Optimization:")
    st.write("Build and optimize machine learning models using evaluation metrics and techniques like cross-validation and grid search.")
    st.write("Ensure models are robust and perform well on unseen data.")
    st.subheader("6.Feature Engineering:")
    st.write("Gain experience in creating new, informative representations of data through feature engineering techniques.")
    st.write("Improve model performance by enhancing the quality of input features.")
    st.subheader("7.Web Application Development:")
    st.write("Develop a web application using the Streamlit module to showcase machine learning models.")
    st.write("Enable users to make predictions on new data through an interactive interface.")
    st.subheader("8.Understanding Manufacturing Domain Challenges:")
    st.write("Learn about the challenges and best practices in the manufacturing domain.")
    st.write("Understand how machine learning can address industry-specific issues and improve decision-making processes.")



