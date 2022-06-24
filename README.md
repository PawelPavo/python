# python

# BLACKJACK
# Switchicng Ace value explained
          '''
          Aces in Blackjack have 2 values 11 or 1, so if we have a self.value of over 21, and self.aces is at least 1, then we deduct 10 from the value, which means               the ace now as a value of 1
          If you have a value of less than 21, then the block of code will not run
          If you are over 21 and you still have an ace
          So lets say that you have 3 cards ace, ace and ace
          So are self.aces value will now be 3
          so 3 aces is 3 x 11 = 33, so we are greater than 21, so as we have 3 aces we deduct 10 from the value of 33, and take 1 ace away from out stash of 3
          So now we have
          self.value is 21
          self.aces is 2
          But we still have 3 aces in our hand, it is just 1 has now been changed to a 1
          So we now check our self.value again, and this time we have
          11 + 11 + 1 which is 23, so we are still greater than 21, so again as we have 2 aces in our stash (self.aces = 2) we can change one of the 2 aces to a 1 by               deducting 10 off self.value. So we now have 1 ace in our stash and a self.value of
          11 + 1 + 1 which is 14, so the block of code is no longer true as we are under 21
          We are not taking the aces from your hand, we are simply adjusting them from an 11 to 1
          So in our scenario here, we still are holding 3 aces in our hand but 1 is valued as an 11 and the other 2 are valued as 1
          So lets now add another card to our hand, lets say as our hand is currently 14, lets add 8, which means our self.value is 23, so its over 21 and we still have           1 ace in our stash, remember we started with 3 aces and have changed from 11's to 1's, so as we can only do that 1 time for each ace, we can still change the             last one from an 11 to a 1, so our self .value is now
          1 + 1 + 1 + 8 so we have a self.value of 11
          So lets take another card, as we have is self.value of 11, lets say we take a 5, then another card which is 9, so we now have a self.value of
          1 + 1 + 1 + 8 + 5 + 9 so we now have a self.value of 25, so we are over 21, but we dont have any more aces in our stash, as we have already changed the 3 we             had, so as it is an and statement, both sides need to the True, so we can no longer adjust for ace
          '''
