from typing import List
import discord
from discord.ext import commands


class TicTacToeButton(discord.ui.Button["TicTacToe"]):
    def __init__(self, x: int, y: int, view):
        super().__init__(style=discord.ButtonStyle.secondary, label="\u200b", row=y)
        self.x = x
        self.y = y
        self._view = view

    @property
    def view(self):
        return self._view

    @view.setter
    def view(self, value):
        self._view = value

    async def callback(self, interaction: discord.Interaction):
        state = self.view.board[self.y][self.x]
        if state in (self.view.X, self.view.O):
            return

        if self.view.current_player == self.view.X:
            self.style = discord.ButtonStyle.danger
            self.label = "X"
            self.view.board[self.y][self.x] = self.view.X
            self.view.current_player = self.view.O
            content = "It is now O's turn"
        else:
            self.style = discord.ButtonStyle.success
            self.label = "O"
            self.view.board[self.y][self.x] = self.view.O
            self.view.current_player = self.view.X
            content = "It is now X's turn"

        self.disabled = True
        winner = self.view.check_board_winner()
        if winner is not None:
            if winner == self.view.X:
                content = "X won!"
            elif winner == self.view.O:
                content = "O won!"
            else:
                content = "It's a tie!"

            for child in self.view.children:
                child.disabled = True

            self.view.stop()

        await interaction.response.edit_message(content=content, view=self.view)


class TicTacToe(discord.ui.View):
    children: List[TicTacToeButton]
    X = -1
    O = 1
    Tie = 2

    def __init__(self):
        super().__init__()
        self.current_player = self.X
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        for x in range(3):
            for y in range(3):
                self.add_item(TicTacToeButton(x, y, self))

    def check_board_winner(self):
        for across in self.board:
            value = sum(across)
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        for line in range(3):
            value = self.board[0][line] + self.board[1][line] + self.board[2][line]
            if value == 3:
                return self.O
            elif value == -3:
                return self.X

        diag = self.board[0][2] + self.board[1][1] + self.board[2][0]
        if diag == 3:
            return self.O
        elif diag == -3:
            return self.X

        diag = self.board[0][0] + self.board[1][1] + self.board[2][2]
        if diag == -3:
            return self.X
        elif diag == 3:
            return self.O

        if all(i != 0 for row in self.board for i in row):
            return self.Tie

        return None


class TicTacToeCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.active_games = {}

    def cleanup_game(self, guild_id: int):
        if guild_id in self.active_games:
            del self.active_games[guild_id]

    @commands.slash_command(name="ttt", description="Play Tic Tac Toe")
    async def tictactoe(self, ctx):
        guild_id = ctx.guild_id
        view = TicTacToe()  # Create a new instance of the TicTacToe view
        self.active_games[guild_id] = view
        await ctx.send("Tic Tac Toe: X goes first", view=view)
        await ctx.respond("Good luck!")
        return



def setup(bot):
    bot.add_cog(TicTacToeCog(bot))

    #test