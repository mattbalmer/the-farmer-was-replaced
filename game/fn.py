from Directions import Direction
from Entities import Entity
from Grounds import Ground
from Items import Item

def can_harvest() -> bool:
    '''
    Used to find out if plants are fully grown.

    returns `True` if there is an entity under the drone that is ready to be harvested, `False` otehrwise.

    takes the time of `1` operation to execute

    example usage:
    .. code-block:: python
    if can_harvest():
        harvest()
    '''
    pass

def clear() -> None:
    '''
    Removes everything from the farm, and moves the drone back to position `(0,0)`.

    returns `None`

    takes the time of `200` operations to execute.

    example usage:
    .. code-block:: python
    clear()
    '''
    pass

def get_entity_type() -> Entity:
    '''
    Find out what kind of entity is under the drone.

    returns `None` if the tile is empty, otherwise returns the type of the entity under the drone.

    takes the time of `1` operation to execute.

    example usage:
    .. code-block:: python
    if get_entity_type() == Entities.Grass:
        harvest()
    '''
    pass

def get_ground_type() -> Ground:
    '''
    Find out what kind of ground is under the drone.

    returns the type of ground under the drone.

    takes the time of `1` operation to execute.

    example usage:
    .. code-block:: python
    if get_entity_type() != Grounds.Soil:
        till()
    '''
    pass

def get_pos_x() -> int:
    '''
    Gets the current x position of the drone.
    The x position starts at `0` in the `West` and increases in the `East` direction.

    returns a number representing the current x coordinate of the drone.

    takes the time of `1` operation to execute.

    example usage:
    .. code-block:: python
    x, y = get_pos_x(), get_pos_y()
    '''
    pass

def get_pos_y() -> int:
    '''
    Gets the current y position of the drone.
    The y position starts at `0` in the `South` and increases in the `North` direction.

    returns a number representing the current y coordinate of the drone.

    takes the time of `1` operation to execute.

    example usage:
    .. code-block:: python
    x, y = get_pos_x(), get_pos_y()
    '''
    pass

def get_world_size() -> int:
    '''
    Get the current size of the farm.

    returns the side length of the grid in the north to south direction.

    takes the time of 1 operation to execute.

    example usage:
    .. code-block:: python
    for i in range(get_world_size()):
        move(North)
    '''
    pass

def harvest():
    '''
    Harvests the entity under the drone.
    If you harvest an entity that can't be harvested, it will be destroyed.

    returns `True` if an entity was removed, `False` otherwise.

    takes the time of `200` operations to execute if an entity was removed, `1` operation otherwise.

    example usage:
    .. code-block:: python
    harvest()
    '''
    pass

def move(direction: Direction) -> bool:
    '''
    Moves the drone into the speicified **direction** by one tile.
    If the drone moves over the edge of the farm it wraps back to the other side of the farm.

    ```
    East  = right
    West  = left
    North = up 
    South = down
    ```

    returns `True` if the drone has moved, `False`, otherwise.

    takes the time of `200` operations to execute if the drone has moved, `1` operation otherwise.

    example usage:
    .. code-block:: python
    move(North)
    '''
    pass

def num_items(item: Item) -> int:
    '''
    Find out how many of `item` you currently have.

    returns the number of `item` currently in your inventory.

    takes the time of `1` operation to execute.

    example usage:
    .. code-block:: python
    if num_items(Items.Fertilizer) == 0:
        trade(Items.Fertilizer)
    '''
    pass

def plant(entity: Entity) -> bool:
    '''
    Plants the specified `entity` under the drone if it can be planted.
    Otherwise it just does nothing.

    returns `True` if it succeeded, `False` otherwise.

    takes the time of `200` operations to execute if it succeeded, `1` operation otherwise.

    example usage:
    .. code-block:: python
    plant(Entities.Bush)
    '''
    pass

def till() -> None:
    '''
    Tills the ground under the drone into `Grounds.Soil`. If it's already soil it will change the ground back to `Grounds.Turf`.

    returns `None`

    takes the time of `200` operations to execute.

    example usage:
    .. code-block:: python
    till()
    '''
    pass

def trade(item: Item, n: int = 1) -> bool:
    '''
    Tries to buy the specified `item`.
    If the `item` cannot be bought or you don't have the required resources it simply does nothing.

    overloads:
    `trade(item)`: buys the `item` once.
    `trade(item, n)`: If `Unlocks.Multi_Trade` is unlocked, this wil buy the `item` `n` times immediately. If you can't afford all `n` items, it won't buy any at all. If `Unlocks.Multi_Trade` is not unlocked, it throws an error.

    returns `True` if it was able to buy the items, `False` otherwise.

    takes the time of `200` operations to execute if it succeeded, `1` operation otherwise.

    example usage:
    .. code-block:: python
    if num_unlocked(Unlocks.Multi_Trade) > 0:
        trade(Items.Carrot_Seed, 10)
    else:
        for i in range(10):
            trade(Items.Carrot_Seed)
    '''
    pass

def use_item(item: Item) -> bool:
    '''
    Attempts to use the specified `item`. Can only be used with some items including `Items.Water_Tank`, `Items.Fertilizer`, and `Items.Egg`.

    returns `True` if an item was used, `False` otherwise.

    takes the time of `200` operations to execute if it succeeded, `1` operation otherwise.

    example usage:
    .. code-block:: python
    use_item(Items.Fertilizer)
    '''
    pass