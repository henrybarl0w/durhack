import pygame
import dealer
import player

class PokerGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Poker Game")
        self.clock = pygame.time.Clock()
        self.game = dealer.Dealer()
        self.running = True
        self.phase = "setup"  # phases: setup, preflop, flop, turn, river, showdown
        self._phase_started = False  # internal flag to track phase start

    def start_game(self):
        self.setup_players()
        self.game.deal()
        self.main_loop()

    def setup_players(self):
        for _ in range(4):
            self.game.players.append(player.Player())
            self.game.players[-1].setMoney(1000)

    def main_loop(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """
        Progresses through a single hand automatically:
          - setup: create players and deal
          - preflop: run preflop betting (blinds posted inside Dealer.betting)
          - flop: deal 3 community cards + betting
          - turn: deal 1 card + betting
          - river: deal 1 card + betting
          - showdown: determine winner, pay pot, reset for next hand

        This is intentionally simple and non-blocking; each phase runs exactly once
        when reached. For more interactive control, switch phases from input/events.
        """
        # Setup: create players and deal one hand
        if self.phase == "setup":
            if not self._phase_started:
                self.setup_players()
                self.game.deal()
                self._phase_started = True
            # move immediately to preflop
            self.phase = "preflop"
            self._phase_started = False
            return

        # Preflop: post blinds and run preflop betting
        if self.phase == "preflop":
            if not self._phase_started:
                self.game.betting(0)   # preflop (0 cards revealed)
                self._phase_started = True
            self.phase = "flop"
            self._phase_started = False
            return

        # Flop: reveal three community cards and run betting
        if self.phase == "flop":
            if not self._phase_started:
                self.game.betting(3)   # flop (3 cards)
                self._phase_started = True
            self.phase = "turn"
            self._phase_started = False
            return

        # Turn: reveal one card and run betting
        if self.phase == "turn":
            if not self._phase_started:
                self.game.betting(1)   # turn (1 card)
                self._phase_started = True
            self.phase = "river"
            self._phase_started = False
            return

        # River: reveal one card and run betting
        if self.phase == "river":
            if not self._phase_started:
                self.game.betting(1)   # river (1 card)
                self._phase_started = True
            self.phase = "showdown"
            self._phase_started = False
            return

        # Showdown: determine winner(s), pay pot, reset and start next hand
        if self.phase == "showdown":
            if not self._phase_started:
                try:
                    winner_index = self.game.findBestHand()
                except Exception:
                    winner_index = None

                if winner_index is not None and 0 <= winner_index < len(self.game.players):
                    self.game.players[winner_index].addMoney(self.game.pot)
                # reset per-player round memory and dealer state for next hand
                for p in self.game.players:
                    p.roundReset()
                self.game.reset()
                # start next hand
                self.game.deal()
                # advance to preflop for the new hand
                self.phase = "preflop"
                self._phase_started = False
            return

    def render(self):
        self.screen.fill((0, 128, 0))  # Green background for poker table
        self.draw_community_cards()
        self.draw_player_cards()
        pygame.display.flip()

    def draw(self, surface):
        """
        Compatibility helper used by main.py: draw the current game state onto
        the provided Surface (window).
        """
        surface.fill((0, 128, 0))
        # community
        for i, card in enumerate(self.game.communityCards):
            card_image = self.load_card_image(card)
            surface.blit(card_image, (100 + i * 100, 50))
        # players
        for i, player_obj in enumerate(self.game.players):
            for j, card in enumerate(player_obj.getCards()):
                card_image = self.load_card_image(card)
                surface.blit(card_image, (100 + j * 100, 200 + i * 100))

    def draw_community_cards(self):
        # Draw community cards on the screen
        for i, card in enumerate(self.game.communityCards):
            card_image = self.load_card_image(card)
            self.screen.blit(card_image, (100 + i * 100, 50))

    def draw_player_cards(self):
        # Draw each player's cards on the screen
        for i, player in enumerate(self.game.players):
            for j, card in enumerate(player.getCards()):
                card_image = self.load_card_image(card)
                self.screen.blit(card_image, (100 + j * 100, 200 + i * 100))

    def load_card_image(self, card):
        # Load the card image based on the card string (e.g., "2H", "AS")
        return pygame.Surface((70, 100))  # Placeholder for card image

if __name__ == "__main__":
    game = PokerGame()
    game.start_game()
    pygame.quit()