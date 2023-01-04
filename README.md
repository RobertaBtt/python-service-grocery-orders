# Python Service Grocery orders
(built from adaptive-python-service)

The output of this service is a list of dictionary.

Each item/dictionary represents an order, for an item, for a day.

An **order** is 
- a collection of information about the item
- when it can be ordered 
- when it will be delivered
- what’s the suggested retail price
- what’s the profit margin
- the purchase price, 
- in which categories this item is in
- any labels
- how much there’s in a case of this stuff
- how much they should order
- how much do they have in the inventory.



![sample_order_dict.jpg](static%2Fsample_order_dict.jpg)

Order quantity =  
(sales quantity prediction at delivery_day - the inventory quantity at ordering_day) / (amount of items in a case (case_content_quantity)).

---------------------------------------
![database_diagram.jpg](static%2Fdatabase_diagram.jpg)
----------------------------------------------------------------
From the **main**.py endpoint it is possible to call the services.


This projects follows the **Repository Pattern**.

It is an abstraction over persistent storage.
Hides the details of data access.

In the dependency inversion the domain model is free from the Infrastructure concerns.

Repository pattern is a simple abstraction
around permanent storage. 


![RepositoryPattern.jpg](static%2FRepositoryPattern.jpg)

The Service Layer orchestrate our workflow and defines the Use Cases of our systems.
The service layer will become the main way to our app.

This is the architecture **Layered Architecture**, of type monolith.

Components are organized into logical horizontal layers and every layer consists of 4 standards layers:

* Presentation
* Business
* Persistence
* Database

![Layers.jpg](static%2FLayers.jpg)

_Layers of isolation: changes made in one layer in the architecture, generally don't impact
or affect components in other layers.
Each layer is independent of the others._



### Environment - POSIX
**Install python3. Last Version is now 3.10.6**

**Create a hidden folder with the local python environment with this command**

`python3 -m venv .local_venv`


**Activate the environment**

`source .local_venv/bin/activate`

**Install the requirements**

`pip3 install -r requirements.txt`

**Run tests**

`python3 -m pytest tests/ -v`

**Run web app**

`python3 web.py`
