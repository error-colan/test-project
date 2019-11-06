import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt



def main():
    st.title("Common Dataset Explorer")
    st.subheader("Datasets Explorer with Streamlit")

    html_temp = """
	<div style="background-color:tomato;"><p style="color:white;font-size:50px;padding:10px">Trial project</p></div>
	"""
    st.markdown(html_temp, unsafe_allow_html=True)



    my_dataset = 'csv/short_data.csv'

    def upload_data(dataset):
        df = pd.read_csv(dataset, index_col=0)
        df['fit.cluster'] = df['fit.cluster'].replace([1, 2, 3, 4], ['High', 'Low', 'Medium', 'Critical'])
        return df

    data = upload_data(my_dataset)

    def check():
        obj_name = st.selectbox("Enter the Object Name:", data['Object_Name'])
        obj_type = st.selectbox("Enter the Object Type:", data['Object_Type'].unique())
        obj_app = st.selectbox("Enter the object Application:", data['Application'].unique())

        sub = data[(data['Object_Name'] == obj_name) & (data['Object_Type'] == obj_type) &
                   (data['Application'] == obj_app)]

        sub_name = sub['Object_Name'].to_string(index=False)
        sub_app = sub['Application'].to_string(index=False)
        sub_type = sub['Object_Type'].to_string(index=False)
        sub_count = sub['COUNT.Version.Changes'].to_string(index=False)
        sub_defect = sub['Defect'].to_string(index=False)
        sub_cluster = sub['fit.cluster'].to_string(index=False)

        def visual():
            st.header("generating plots")

            selection_a = st.selectbox("choose the application:", data['Application'].unique())
            selection_typo = st.selectbox("choose the application:", data['Object_Type'].unique())

            if selection_a:
                if selection_typo:
                    cust = data[(data['Application'] == selection_a) & (data['Object_Type'] == selection_typo)]

                if st.checkbox("data"):
                    st.write(cust)

                if st.button("Generate Plot"):
                    st.success("Generating Customizable Plot of  application '**{}**' and object type '**{}**'"
                               .format(selection_a, selection_typo))

                    cust_data = cust['fit.cluster']

                    st.header('histogram')
                    plt.hist(cust_data, bins=10)

                    plt.xlabel('cluster')
                    # frequency label
                    plt.ylabel('frequency')
                    # plot title
                    plt.title('visual data')
                    st.pyplot()

                    st.write(cust.iloc[:, -1].value_counts())

        if sub.empty:
            st.error("The Object name, type and application does not match.")
            st.warning("Does not Match")
            visual()

        else:
            st.success("**object name is:**" + sub_name)
            st.success("**object name is:**" + sub_type)
            st.write('**object name is:**', sub_name)
            st.write('Application number is :', sub_app)
            st.write('Object Type is :', sub_type)
            st.write('Count number is :', sub_count)
            st.write('Defect is :', sub_defect)
            st.write('Cluster is :', sub_cluster)

    check()

    st.sidebar.header("About App")
    st.sidebar.info("A Simple EDA App for Exploring Common ML Dataset")

    st.sidebar.header("About")
    st.sidebar.info("Mini Project")
    st.sidebar.text("Built with Streamlit")
    st.sidebar.text("Maintained by Shubham Rathore")


if __name__ == '__main__':
    main()


