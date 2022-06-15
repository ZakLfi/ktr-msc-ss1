package exceptions;

import java.util.List;

public abstract class Character implements Movable {
	
	private String name; 
	private final String RPGClass ; 
	protected int life; 
	protected int agility; 
	protected int strength; 
	protected int wit ; 
	
	public Character(String name, String RPGClass) {
		this.name = name ;
		this.RPGClass = RPGClass ; 
		this.life = 50 ; 
		this.agility =  2 ; 
		this.strength = 2 ; 
		this.wit = 2 ; 
		announcement(); 
	}
	
	public String getName() { return name ; }
	
	public String getRPGClass() { return RPGClass ; }

	public int getLife() { return life ; }

	public int getAgility() { return agility ; }

	public int getStrength() { return strength ; }

	public int getWit() { return wit ; }
	
	public void attack(String weapon) throws WeaponException {
		if(weapon.isEmpty())
			throw new WeaponException(name + ": I refuse to fight with my bare hands ."); 
		if(! acceptedWeapons().contains(weapon)) {
			throw new WeaponException(name + weaponDontFitCharacter(weapon)); 
		}
		System.out.println(name + ": Rrrrrrrrr ...."); 
		anouncingAttack(weapon); 
	}
		
	protected abstract void announcement(); 
	
	public void moveRight() {
		System.out.println(characterMoving() + " right " + movingStyle());
	}
	public void moveLeft() {
		System.out.println(characterMoving() + " left " + movingStyle());
	}
	public void moveForward() {
		System.out.println(characterMoving() + " forward " + movingStyle());
	}
	public void moveBack() {
		System.out.println(characterMoving() + " back " + movingStyle());
	}
	
	private String characterMoving() {
		return this.getName() + ": moves "; 
	}
	
	protected abstract String movingStyle(); 
	
	protected final void unsheathe() {
		System.out.println(this.getName() + "unsheathes his weapon ."); 
	}
	
	protected abstract String weaponDontFitCharacter(String weapon); 
	
	protected void tryToAttack(String weapon) {
		try {
			attack(weapon); 
		}catch(WeaponException e) {
			System.out.print(e.getMessage());
		}
	}
	
	protected abstract List<String> acceptedWeapons(); 
	
	protected void attackMessage(String weapon) {
		if(acceptedWeapons().contains(weapon))
			anouncingAttack(weapon);
			
	}
	
	protected abstract void anouncingAttack(String message); 

}
