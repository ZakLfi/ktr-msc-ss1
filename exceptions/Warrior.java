package exceptions;

import java.util.List;

public class Warrior extends Character {

	public Warrior(String name) {
		super(name, "Warrior");
		this.life = 100;
		this.strength = 10; 
		this.agility = 8; 
		this.wit = 3;
	}
	
	@Override
	protected void anouncingAttack(String weapon) {
		System.out.println(this.getName() +": I'll crush you with my "+weapon+ " !"); 
	}
	
	@Override
	protected void announcement() {
		System.out.println(this.getName()+": My name will go down in history !"); 
	}
	
	@Override
	protected String movingStyle() {
		return "like a bad boy."; 
	}

	@Override
	protected String weaponDontFitCharacter(String weapon) {
		return ": A "+ weapon +" ?? What should I do with this ?!\n";
	}

	@Override
	protected List<String> acceptedWeapons() {
		return List.of("hammer", "sword"); 
	}
	
	
	

}
