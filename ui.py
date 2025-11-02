import pygame
from dealer import Dealer
from player import Player

class PokerUI:
    def __init__(self, width=800, height=600):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Poker Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.dealer = Dealer()
        self.players = [Player() for _ in range(4)]
        self.running = True

    def draw_cards(self):
        # Draw community cards
        for i, card in enumerate(self.dealer.communityCards):
            card_image = self.load_card_image(card)
            self.screen.blit(card_image, (100 + i * 100, 50))

        # Draw player cards
        for i, player in enumerate(self.players):
            for j, card in enumerate(player.getCards()):
                card_image = self.load_card_image(card)
                self.screen.blit(card_image, (100 + i * 100, 150 + j * 100))

    def load_card_image(self, card):
        # Placeholder for loading card images
        return pygame.Surface((70, 100))  # Replace with actual image loading

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((0, 128, 0))  # Green background for poker table
            self.draw_cards()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

if __name__ == "__main__":
    ui = PokerUI()
    ui.run()