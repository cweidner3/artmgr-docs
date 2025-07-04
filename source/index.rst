Art Manager documentation
=========================

!NOTICE!

This project is still being initially brought up and is not quite
ready for any serious adoptions.

!NOTICE!

This application is aimed towards artists interested in maintaining a database
of information on the works created. This provides methods for keeping track of
what has been sold as well as what works are still avaliable and where they are
located.

.. figure:: _static/window_views/app-overview.png

   Art Manager Application Running

Peices can be grouped into "Series" to allow for grouping works into
collections of peices with a particular theme. They may also be grouped into
exhibits to allow for keeping track of what will be taken to a showing, market,
ect. or for when looking back at events in the past.

When attaching images, this application has built image manipulation to resize
the digital images to optimize the data usage within the database as well as
loading times within the application. Note, this application is not intended to
maintain unaltered images of works; this utilizes the images to provide easier
identification of each entry with the works they should represent.

The source for the application is kept in version control in the
`Art Manager Repo`_. While the source for this documentation is kept in the
`Documentation Repo`_.

.. _Art Manager Repo: https://gitlab.corara.mooo.com/desktop-apps/art-manager

.. _Documentation Repo: https://gitlab.corara.mooo.com/desktop-apps/art-manager-docs

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   components/index.rst
