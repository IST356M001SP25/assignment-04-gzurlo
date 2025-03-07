'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

# TODO Write code here to complete the unibrow.py
'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl  # Import helper functions

# Streamlit App Title & Subtitle
st.title("📊 UniBrow")
st.caption("The Universal Data Browser")

# Upload File Section
uploaded_file = st.file_uploader("📂 Upload a dataset", type=["csv", "xlsx", "json"])

if uploaded_file:
    # Determine file type and load data
    file_extension = pl.get_file_extension(uploaded_file.name)
    df = pl.load_file(uploaded_file, file_extension)

    if df is not None:
        st.success(f"✅ Loaded {uploaded_file.name} successfully!")

        # Column Selection
        all_columns = pl.get_column_names(df)
        selected_columns = st.multiselect("📝 Select columns to display:", all_columns, default=all_columns)

        # Row Filtering (Toggle)
        apply_filter = st.checkbox("🔍 Apply a row filter?")
        if apply_filter:
            # Choose a text column for filtering
            object_columns = pl.get_columns_of_type(df, 'object')
            if object_columns:
                filter_column = st.selectbox("🔠 Select a column to filter:", object_columns)
                unique_values = pl.get_unique_values(df, filter_column)
                filter_value = st.selectbox(f"🆎 Select a value from '{filter_column}':", unique_values)

                # Apply the filter
                df = df[df[filter_column] == filter_value]

        # Display the Filtered DataFrame
        st.subheader("📋 Processed DataFrame")
        st.dataframe(df[selected_columns])

        # Show Summary Statistics
        st.subheader("📊 Data Summary")
        st.write(df[selected_columns].describe())

    else:
        st.error("⚠️ Could not load file. Please check the format.")

else:
    st.info("📥 Upload a CSV, XLSX, or JSON file to get started.")

