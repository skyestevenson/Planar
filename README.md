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
