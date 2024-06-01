#include <iostream>
#include <vector>
#include <cstdlib>
#include <random>
#include <ctime>

using namespace std;

class Card{
    public:
        string value;
        string suit;
        int intValue;

        Card(string v,string s,int i) : value(v),suit(s),intValue(i) {}

        string getCardString(){
            return this->suit + this->value + '(' + to_string(this->intValue) + ')';
        }
};

class Deck{
    private:
        vector<Card> deck;        
    public:
        Deck() {
            deck=generateDeck();
        };
        
        vector<Card> generateDeck(){
            vector<Card> newDeck;
            vector<string> values={"A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"};
            vector<string> suits={"♣", "♦", "♥", "♠"};

            for(auto suit : suits){
                for(int j=0;j<values.size();++j){
                    Card card1(values[j],suit,j+1);
                    newDeck.push_back(card1);
                }
            }
            return newDeck;
        }

        void printDeck(){
            cout << "Displaying cards...";
            for(int i=0;i<deck.size();++i){
                cout << deck[i].getCardString() << endl;
            }
        }

        Card draw(){
            Card fin=deck.back();
            deck.pop_back();
            return fin;
        }

        void shuffleDeck(){
            int deckSize=deck.size();
            srand(time(0));
            int randomInt=rand()%(deckSize+1);
            
            for(auto i=0;i<deckSize;++i){
                int j=i+rand()/((RAND_MAX / (deck.size()-i))+1);
                swap(deck[i],deck[j]);    }

}
};

class Dealer{
    private:
        struct Table{
            vector<vector<Card>> players;
            Deck deck;
        };
    public:
        static vector<vector<Card>> startGame(int amountOfPlayers){
            Table table;
            table.deck.shuffleDeck();
            for(int i=0;i<amountOfPlayers;++i){
                vector<Card> playerCard;
                for(int j=0;j<2;++j){
                    playerCard.push_back(table.deck.draw());
                    }
                table.players.push_back(playerCard);
            }
            return table.players;
        }
};

int main(){
    Deck card1;
    card1.printDeck();
    cout << "shuffling deck ..." << endl;
    card1.shuffleDeck();
    card1.printDeck();

    cout << "Drawing a card .." << endl;
    cout << card1.draw().getCardString() << endl;

    cout << "Card of a person" << endl;

    vector<vector<Card>> table =Dealer::startGame(2);
    for(int i=0;i<2;++i){
        cout << table[0][i].getCardString() << endl;
    }
    
}