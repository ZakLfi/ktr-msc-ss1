package exceptions;

import java.util.List;

public class Mage extends Character {

	public Mage(String name) {
		super(name, "Mage");
		this.life = 70;
		this.strength = 3 ;
		this.agility = 10 ; 
		this.wit = 10 ;
	}

	@Override
	protected void anouncingAttack(String weapon) {
		System.out.println(this.getName() +": Feel the power of my "+weapon+ "!");
	}
	
	@Override
	protected void announcement() {
		System.out.println(this.getName()+": May the gods be with me."); 
	}
	
	@Override
	protected String movingStyle() {
		return "furtively."; 
	}

	@Override
	protected String weaponDontFitCharacter(String weapon) {
		return ": I don 't need this stupid "+ weapon +"! Don 't misjudge my powers !\n";
	}

	@Override
	protected List<String> acceptedWeapons() {
		return List.of("magic", "wand"); 
	}
	
	

}
