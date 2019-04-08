# Planar
Engine-Agnostic Virtual World Markup Language

Basic structure of Planar:
- plane
  - global_properties
    - name (string)
    - population_max (integer)
    - boundaries
      - x (tuple, 2 integers)
      - y (tuple, 2 integers)
      - z (tuple, 2 integers)
    - gravity (float)
  - objects
    - uuid #
      - asset (string)
      - transform
        - t (tuple, 3 floats)
        - r (tuple, 3 floats)
        - s (tuple, 3 floats)
      - physics_enabled (boolean)

TODO:
- Dependency system
  - list all assets referenced in scene at the top of the file
  - add assets to list on add_object()
  - remember the URLs for web-based assets and have, on init, the program download all missing assets into the plane's folder
- Abstractify (you heard me) assets vs their sources
  - Asset #UUID has source "PATH"
  - "PATH" can change, #UUID cannot
