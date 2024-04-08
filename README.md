# OnDemand Bot

This bot is used for automating the RIT OnDemand website to make ordering food easier and more convenient.

NOTE: This bot is a work in progress, as such ordering is currently unavailable.
      Commands to view menus and hours are currently working.

## Commands

### 1. Starting a New Order
- **Command**: `/startorder`
- **Description**: Initiates a new food order.
- **Usage**:
  - Type `/startorder` to begin the order process.
  - After initiating an order, you can enter the items you wish to order directly into the chat.

### Ordering Process
After starting an order with `/startorder`, you can type the items you want to order directly into the chat. The bot will process each message as a part of your order until you finalize it with `/endorder`.

For example:
- `restaurant=The Commons, burger, fries` - This will set your restaurant to 'The Commons' and add 'burger' and 'fries' to your order.
- Remember to specify the restaurant first in your order.
- The bot will recognize abbreviated restaurant names and menu items.

### 2. Ending an Order
- **Command**: `/endorder`
- **Description**: Completes your current order.
- **Options**:
  - `payment_info`: Your payment information or method.
- **Usage**:
  - To finalize your order, type `/endorder [payment_info]`. Replace `[payment_info]` with your actual payment details.

### 3. Getting Restaurant Hours
- **Command**: `/hours`
- **Description**: Retrieves the operating hours of a specific restaurant.
- **Options**:
  - `restaurant`: Name of the restaurant.
- **Usage**:
  - For hours, type `/hours restaurant:[restaurant_name]`. Replace `[restaurant_name]` with the name of the restaurant.

### 4. Viewing Restaurant Menu
- **Command**: `/menu`
- **Description**: Displays the menu of a specific restaurant.
- **Options**:
  - `restaurant`: Name of the restaurant.
- **Usage**:
  - To view a menu, type `/menu restaurant:[restaurant_name]`.

### 5. Listing Available Restaurants
- **Command**: `/restaurants`
- **Description**: Provides a list of all available restaurants.
- **Usage**:
  - Type `/restaurants` to see a list of all available restaurants.

### 6. Help Information
- **Command**: `/help`
- **Description**: Shows help information about using the bot.
- **Usage**:
  - Type `/help` to view this help guide.
