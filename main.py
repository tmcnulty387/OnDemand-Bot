import interactions
import os
from fetch import fetch_hours, restaurants, fetch_menus
from order import OrderManager

bot = interactions.Client(token=os.getenv('TOKEN'))
# active_orders = {}

# @bot.command(
#     name="startorder",
#     description="Start a new order"
# )
# async def start_order(ctx: interactions.CommandContext):
#     user_id = ctx.author.id
#     if user_id not in active_orders:
#         order_manager = OrderManager()
#         if order_manager.initialization_successful:
#             active_orders[user_id] = order_manager
#             await ctx.send("Order started! Add items and finalize your order with /endorder.")
#         else:
#             await ctx.send("Failed to start order due to WebDriver issues.")
#     else:
#         await ctx.send("You already have an active order. Use /endorder to finalize it.")

# @bot.command(
#     name="endorder",
#     description="Complete your order",
#     options=[
#         interactions.Option(
#             name="payment_info",
#             description="Your payment information",
#             type=interactions.OptionType.STRING,
#             required=True
#         )
#     ]
# )
# async def end_order(ctx: interactions.CommandContext, payment_info: str):
#     user_id = ctx.author.id
#     if user_id in active_orders:
#         order = active_orders.pop(user_id)
#         # Here, you would process the order and payment info
#         await ctx.send(f"Order completed! Payment info received: {payment_info}. Items ordered: {order['items']}")
#     else:
#         await ctx.send("You don't have an active order. Start a new order with /startorder.")

# @bot.event
# async def on_message(message):
#     if message.author.bot:
#         return

#     user_id = message.author.id
#     if user_id in active_orders:
#         response = new_order(user_id, message.content)
#         await message.channel.send(response)

@bot.command(
    name="hours",
    description="Get the hours of a specific restaurant",
    options=[
        interactions.Option(
            name="restaurant",
            description="Name of the restaurant",
            type=interactions.OptionType.STRING,
            required=True
        )
    ]
)
async def hours(ctx, restaurant: str):
    hours = fetch_hours(restaurant)
    if not hours:
        await ctx.send("Restaurant hours not found")
    else:
        await ctx.send(hours)

@bot.command(
    name="menu",
    description="Get the menu of a specific restaurant",
    options=[
        interactions.Option(
            name="restaurant",
            description="Name of the restaurant",
            type=interactions.OptionType.STRING,
            required=True
        )
    ]
)
async def menus(ctx, restaurant: str):
    menu = fetch_menus(restaurant)
    if not menu:
        await ctx.send("Menu was not found")
    else:
        await ctx.send(menu)

@bot.command(
    name="help",
    description="Get help information"
)
async def help(ctx):
    with open("README.md", "r") as file:
        help_content = file.read()
    await ctx.send(help_content)

@bot.command(
    name="restaurants",
    description="Get a list of available restaurants"
)
async def restaurant(ctx):
    restaurant_list = '\n'.join(restaurants.keys())
    await ctx.send(restaurant_list)

bot.start()
