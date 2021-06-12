.. image:: https://api.codeclimate.com/v1/badges/d3b45d533e395beba9d8/maintainability
   :target: https://codeclimate.com/github/stanislavglazko/linked_list/maintainability
   :alt: Maintainability

.. image:: https://api.codeclimate.com/v1/badges/d3b45d533e395beba9d8/test_coverage
   :target: https://codeclimate.com/github/stanislavglazko/linked_list/test_coverage
   :alt: Test Coverage

======================
Linked List for Python
======================

There is my own version of doubly linked list.
----------------------------------------------

Attributes of doubly linked list:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* head = the head element (start of the doubly linked list)
* tail = the tail element (end of the doubly linked list)
* length

Methods of doubly linked list:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* add_at_tail = add new element at the tail with val(int)

Example:

.. code-block:: python

   linked_list.add_at_tail(4)

* add_at_head = add new element at the head with val(int)

Example:

.. code-block:: python

   linked_list.add_at_head(4)

* add_at_index = add new element at the index (int) with val(int)

Example:

.. code-block:: python

   linked_list.add_at_index(0, -1)


* delete_at_index = delete element with the index (int)

Example:

.. code-block:: python

   linked_list.delete_at_index(0)

* get = get the value of the element with the index (int)

Example:

.. code-block:: python

   linked_list.get(0)
