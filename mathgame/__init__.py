from game import Game
def main():
    g = Game()
    while g.running:
        g.new()
        
if __name__ == "__main__":
    main()