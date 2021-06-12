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

.. code-block:: python

   linked_list.add_at_tail(4)

* add_at_head = add new element at the head with val(int)

.. code-block:: python

   linked_list.add_at_head(4)

* add_at_index = add new element at the index (int) with val(int)

.. code-block:: python

   linked_list.add_at_index(0, -1)


* delete_at_index = delete element with the index (int)

.. code-block:: python

   linked_list.delete_at_index(0)

* get = get the value of the element with the index (int)

.. code-block:: python

   linked_list.get(0)

Example of using:

.. code-block:: python

    linked_list = LinkedList()
    linked_list.add_at_tail(1)
    linked_list.add_at_head(2)
    linked_list.add_at_head(3)
    linked_list.add_at_tail(4)
    linked_list.add_at_index(4, 5)
    linked_list.add_at_index(0, -1)
    linked_list.add_at_index(1, -2)
    linked_list.delete_at_index(0)
    linked_list.delete_at_index(5)
    linked_list.delete_at_index(1)
    print(linked_list.get(1))


You are able to get the reversed copy of the linked list.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   reversed_linked_list = reverse_linked_list(linked_list)

You are able to use for cycle for linked list.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. code-block:: python

    linked_list = LinkedList()
    linked_list.add_at_tail(2)
    linked_list.add_at_head(1)
    linked_list.add_at_tail(3)
    linked_list.add_at_tail(4)
    result = []
    for i in linked_list:
        result.append(i)

