import player_main_attr as player
import player_main_stats as stats

theosis = player.PlayerAttr("Theosys", 0)


#Testing getters and setters#
print(theosis.getName())
theosis.setName("Testing")
print(theosis.getName())

#Testing Getters and Setters for player stats#
print(theosis.getPlayerStats().getStrength())