Of course. Let's dive into the details of **Phase 1**. This foundational phase is all about gathering your raw materials (the data) and defining your tools for measurement (the metrics). Getting this right is crucial for the success of the entire project.

Here’s a detailed, step-by-step breakdown of everything you need to do.

---

### **Task 1: Dataset Collection and Preparation** 📚

The goal here isn't just to download files, but to select, understand, and clean a diverse set of data that will robustly test your models.

#### **Action 1.1: Select Your Datasets**
You need to choose **4-5 multi-domain, multivariate time-series datasets**. Diversity is key. A good mix would be:
* **Domain:** At least 3 different fields (e.g., Energy, Finance, Healthcare).
* **Frequency:** Different time intervals (e.g., hourly, daily).
* **Dimensionality:** Varying number of features (one with a few features, one with many).

**Recommended Set (as discussed):**
1.  **ETT (Energy):** Start with **ETTh1** (hourly data). It's the standard benchmark.
2.  **Weather (Climate):** A classic dataset with clear seasonal patterns.
3.  **S&P 500 Stocks (Finance):** Introduces the challenge of non-stationary data.
4.  **Daily Patient Visits (Healthcare):** A simpler, real-world dataset from a different domain.

#### **Action 1.2: Data Preprocessing**
Once you download the CSV files, you must clean and prepare them for the models. This is a critical step.

1.  **Handle the Time Column:** Ensure your date/time column is correctly formatted. When you load the data in `pandas`, use `parse_dates=['your_date_column']` to convert it into a proper datetime object. Set this column as the DataFrame index (`df.set_index('your_date_column', inplace=True)`). This makes time-based operations much easier.
2.  **Deal with Missing Values:** Real-world data is often incomplete. You can't feed `NaN` values to a neural network. For time series, a good strategy is **forward-fill** (`df.fillna(method='ffill')`), which carries the last known value forward. This often makes sense as sensor readings or stock prices don't usually change drastically from one step to the next.
3.  **Normalize the Data:** Neural networks train best when input features are on a similar scale. You should normalize your data after splitting it.
    * **Standardization (Z-score normalization)** is the most common method. For each feature, you calculate the mean ($\mu$) and standard deviation ($\sigma$) *from the training set only* and then scale the data using the formula:
        $$X_{\text{scaled}} = \frac{X - \mu}{\sigma}$$
    * You then use the **same mean and standard deviation** from the training set to transform your validation and test sets. This prevents any information from the test set "leaking" into your training process.
4.  **Split the Data Chronologically:** For time-series data, you **cannot** split it randomly. You must respect the temporal order to prevent the model from training on future data to predict the past. A standard chronological split is **70% for training, 15% for validation, and 15% for testing**.

#### **TA Verification Deliverable 1:**
Prepare a short document or presentation slide that lists your chosen datasets. For each dataset, include:
* **Name and Domain:** (e.g., "ETTh1 - Energy").
* **Source:** A direct link to where you got it.
* **Description:** A brief overview (e.g., "Hourly electricity transformer data with 7 features").
* **Preprocessing Steps:** A clear statement of how you handled missing values and normalization.

---

### **Task 2: Performance Metrics Definition** 📏

Here, you define exactly how you will measure "success." This involves choosing metrics for both the model's accuracy and its efficiency.

#### **Action 2.1: Define Forecasting Accuracy Metrics**
These metrics tell you how close your model's predictions are to the actual values. The two most essential metrics are:

* **Mean Absolute Error (MAE):**
    * **Formula:** $MAE = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|$
    * **What it means:** It's the average absolute difference between the predicted values ($\hat{y}_i$) and the actual values ($y_i$). It's easy to understand because it's in the same units as the original data (e.g., an MAE of 0.5 for temperature means the forecast is off by an average of 0.5 degrees).
* **Mean Squared Error (MSE):**
    * **Formula:** $MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$
    * **What it means:** It's the average of the squared differences. By squaring the error, it **penalizes larger errors much more heavily** than smaller ones. This is useful if you want to ensure your model avoids making significant mistakes.

#### **Action 2.2: Define Resource Efficiency Metrics**
These metrics measure the "cost" of running your models, which is central to your project's goal of creating a resource-efficient student model.

* **Model Size (MB):**
    * **What it means:** The physical space the model's saved weights file takes up on disk.
    * **How to measure:** Simply check the file size of your saved model (e.g., `checkpoint.pth`). A smaller size means the model is more portable and easier to deploy.
* **Inference Time (ms/sample):**
    * **What it means:** How long it takes for the model to make a single prediction on a new piece of data. This is critical for real-time applications.
    * **How to measure:** Run the model on your entire test set, measure the total time taken, and divide by the number of samples in the test set. Be sure to run this on the same hardware for both the teacher and student for a fair comparison.

#### **TA Verification Deliverable 2:**
Finalize a list of the metrics you will use. Prepare a simple list like this to confirm with your TAs:
* **Forecasting Accuracy:** MAE, MSE.
* **Resource Efficiency:** Model Size (MB), Inference Time (ms/sample).

Completing these two tasks in Phase 1 will give you a solid and well-defined foundation to build upon in the subsequent phases.
