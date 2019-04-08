# Planar
Engine-Agnostic Virtual World Markup Language

Planar is a standardized way of storing basic information needed to construct realtime 3D environments in a way that, conceivably, could be integrated into multiple engines/clients so that virtual worlds can be independent from proprietary scaffolding. It's to 3D environments what HTML is to webpages.

Planar outputs a dictionary-based abstraction of a 3D scene to JSON, including references to assets, 3D transformations, physics states, etc.

Basic structure of Planar:
- plane
  - assets
    - paths
  - global_properties
    - name (string)
    - boundaries
      - x (tuple, 2 integers)
      - y (tuple, 2 integers)
      - z (tuple, 2 integers)
    - gravity (float)
    - skybox
      - asset
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
  - remember the URLs for web-based assets and have, on init, the program download all missing assets into the plane's folder
- Abstractify (you heard me) assets vs their sources
  - Asset #UUID has source "PATH"
  - "PATH" can change, #UUID cannot
  - This would allow for changing the source files of assets, while making sure every "cup" in the scene remains a "cup" without major surgery
- Overworld
  - 2D grid of coordinates, hosted online, with each coordinate associated with a particular Plane
  - client for accessing it
  - user uploaded Planes
- Standardized package system for each Plane
  - Single file
