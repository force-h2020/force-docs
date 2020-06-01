Traits and TraitsUI
===================

Traits is a python package, developed by Enthought, for creating and interacting with
statically-typed variables: '**traits**'. To efficiently develop UIs for traits
Enthough developed a sister package, TraitsUI.

A class that has traits variables as attributes, inherits from ``HasTraits``,
so that those variables can be initialized and handled appropriately. Most, if not all,
of the classes in the BDSS (and in the Workflow Manager) inherit from ``HasTraits``,
therefore before extending BDSS it is useful to have some basic knowledge of Traits and
TraitsUI.

Full documentation can be found here:

`Traits <https://docs.enthought.com/traits/>`_

`TraitsUI <https://docs.enthought.com/traitsui/traitsui_user_manual/index.html#contents>`_

These provide brief introductions to the packages. Here we provide an even more
minimal introduction that should make the code examples in following topics clearer.

Traits
------
Traits are class objects (like every variable in python). The more common classes just
wrap around a built-in python type, with a class name that is the capitalised version
of the built-in type. For instance, ::

    # initialization of a string trait, x.
    x = Str('hello world')

    # initialization of a dictionary trait, y.
    y = Dict({'English':'hello world', 'German':'hallo welt'})

    # initialization of a float trait, z, to the default value of 0.0
    z = Float()
    print(z)
    >> 0.0

Traits are typically initialized within a ``HasTraits`` class, ::

    class HelloWorld(HasTraits):

        x = Str('bonjour le monde')

        .....

The ``HasTraits`` inheritence defines a constructor that takes the traits as
arguments. ::

    my_hello_world = HelloWorld(x='ciao mondo', .....)

    print(my_hello_world.x)

    >> ciao mondo

If no argument is given for a trait it is initialized to the value (default or otherwise)
given within the class declaration, ::

    my_hello_world = HelloWorld()

    print(my_hello_world.x)

    >> bonjour le monde

Almost all classes in the BDSS and the Workflow Manager (including all those in the code
examples in the following topics) inherit from ``HasTraits``, usually indirectly through
a base class (you won't see ``HasTraits`` in the class declaration).

Views
-----

TraitsUI provides the UI to traits (as the name suggests!). It provides any
``HasTraits`` object with a default UI that exposes all the traits it contains. Each
trait type is associated with a default UI element (text field for a Str, etc.) and
TraitsUI lays out these elements automatically in a window or panel.

A custom layout, possibly including custom UI elements ('editors'), can be provided by
intializing a ``View`` object within the ``TraitsUI`` class, ::

    class HelloWorld(HasTraits):

        x = Str('bonjour le monde')

        y = Int(5)

        view = View(
            Item(name='x', label='hello message', editor=HTMLEditor()),
            Item(name='y', label='number of people listening'),
            padding=10,
            resizable=True
        )

Each trait is associated with an ``Item`` object (itself a ``HasTraits`` class) by
assigning the ``Item`` 's ``name`` attribute to the string of the trait
variable name. In addition, the ``Item`` constructor has optional arguments that
determine what non-default UI elements ('editors'), if any, are used to expose
the trait and how they are laid out.

The ``Item`` s are assigned to a ``View`` object as * vargs. In addition the ``View``
constructor has a number of optional keyword arguments that determine layout, etc.

For layout purposes ``Item`` s can be grouped by assigning them to ``Group`` objects
that are then assigned to the ``View``. ::

    view = View(
        Group(
            Item(name='x', label='hello message'),
            Item(name='y', label='number of people arriving'),
            label='arriving'
        ),
        Group(
            Item(name='i', label='goodbye message'),
            Item(name='j', label='number of people departing'),
            label='departing'
        )
    )

Like for the ``View``, the ``Group`` constructor has a number of keyword arguments that
effect layout, labelling, etc.

In the following topics, code examples with  ``View`` initializations will show the
resulting UI alongside.
