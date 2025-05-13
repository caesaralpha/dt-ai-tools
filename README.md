# dt-ai-tools

## Running the Application Online

1. Submit the job to run the app using the following command:
    ```bash
    sbatch src/run_streamlit.sh
    ```

2. Check the job status on the dashboard to identify the node where the job is running. Take note of the node name.

## Setting Up Remote Desktop

1. Create a remote desktop session via OnDemand. No high specifications are required.

2. Launch the remote desktop and open a terminal. Use the following command to establish an SSH tunnel:
    ```bash
    ssh -L 8501:localhost:8501 airawan@<node_name>
    ```
    Replace `<node_name>` with the name of the node where the job is running.

3. Open a browser within the remote desktop and navigate to:
    ```
    http://localhost:8501/
    ```
    This will open the application dashboard.