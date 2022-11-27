
# Creating a new Compare Project

* In the `Compare` screen, you can see a button `Create a new Project`
    - ![Screenshot](../assets/compares/compare-init.png){: style="width:360px"}

* Once you have clicked to create a new `Compare` project a new screen will show up to you:
    - ![Screenshot](../assets/compares/create-new-compare-project.png)

* This will walk the user through the data store configurations and which fields should be compared. 

!!! note 
    Once configuration is completed, you can create new Comparison runs, where data stores are compared to each other with a snapshot in time

![Screenshot](../assets/compares/selected-compare-project.png)

* You can see more details of each run clicking in `View Run Details` button.

![Screenshot](../assets/compares/view-run-details.png)


* Each Run will highlight a few details:
    * `Tables Passing`.
    * `Tables Missing`.
    * `Tables Failing`.

---

# Tables Passing 

* Highlights which tables and underlying data were equivalent between the two.

![Screenshot](../assets/compares/tables-passing.png)

# Tables Missing

* Exist on the Baseline data store, but are missing from the Copy data store.

![Screenshot](../assets/compares/tables-missing.png)

# Tables Failing

* Exist on the Baseline data store, but are missing from the Copy data store.

![Screenshot](../assets/compares/tables-failing.png)

* You can see more details of the field when clicking in `Data doesn't match` button.

![Screenshot](../assets/compares/data-doesnt-match.png)