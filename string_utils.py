"""
Module de transformation et de normalisation de données machines.

Ce module fournit plusieurs fonctions utilitaires permettant de :
- convertir certaines valeurs de spécifications (miles → mètres),
- ajouter une section d'informations de contact,
- reformater les dates de maintenance,
- normaliser les identifiants machines (machine_id).

Fonctions fournies
------------------
convert_miles_km(dico)
    Convertit des valeurs en miles vers des valeurs en mètres.

ajout_info(dico)
    Ajoute une section 'contact_information' avec des champs vides.

update_date(dico)
    Reformate les dates (YYYY-MM-DD → DD/MM/YYYY) et normalise le machine_id.

format_machine_id(machine)
    Met sous forme standardisée l'identifiant de la machine (zfill sur 3 chiffres).
"""


def convert_miles_km(dico: dict) -> dict:
    """
    Convert selected specifications from miles to meters.

    This function takes a dictionary containing machine specifications in miles
    and converts the following keys to meters:
    - "depth_capacity_miles" → "depth_capacity_meters"
    - "drilling_speed_miles_per_day" → "drilling_speed_meters_per_day"

    The original mile-based keys are removed.

    Parameters
    ----------
    dico : dict
        Dictionary containing the machine specifications.

    Returns
    -------
    dict
        Updated dictionary with values converted to meters.
    """
    dico["specifications"]["depth_capacity_meters"] = (
        dico["specifications"]["depth_capacity_miles"] * 1609
    )
    dico["specifications"]["drilling_speed_meters_per_day"] = (
        dico["specifications"]["drilling_speed_miles_per_day"] * 1609
    )

    del dico["specifications"]["depth_capacity_miles"]
    del dico["specifications"]["drilling_speed_miles_per_day"]

    return dico


def ajout_info(dico: dict) -> dict:
    """
    Add an empty contact information section to the machine dictionary.

    The added "contact_information" field includes:
    - operator_company
    - contact_person
    - phone
    - email

    All fields are initialized to None.

    Parameters
    ----------
    dico : dict
        Dictionary representing the machine.

    Returns
    -------
    dict
        Updated dictionary including the contact information section.
    """
    dico["contact_information"] = {
        "operator_company": None,
        "contact_person": None,
        "phone": None,
        "email": None,
    }
    return dico


def update_date(dico: dict) -> dict:
    """
    Reformat maintenance dates and standardize machine ID.

    - Dates in the format 'YYYY-MM-DD' are converted to 'DD/MM/YYYY'
      for both:
        * last_maintenance_date
        * next_maintenance_due

    - The machine_id is reformatted by zero-padding the numeric suffix to
      three digits (e.g., 'TX-7' → 'TX-007').

    Parameters
    ----------
    dico : dict
        Dictionary containing machine maintenance data.

    Returns
    -------
    dict
        Updated dictionary with formatted dates and machine ID.
    """
    # Reformatting dates
    dico["last_maintenance_date"] = "/".join(
        dico["last_maintenance_date"].split("-")[::-1]
    )
    dico["next_maintenance_due"] = "/".join(
        dico["next_maintenance_due"].split("-")[::-1]
    )
    return dico


def format_machine_id(machine: dict) -> dict:
    """
    Standardize the machine ID format by zero-padding its numeric part.

    Example
    -------
    'AB-5' → 'AB-005'
    'XY-42' → 'XY-042'

    Parameters
    ----------
    machine : dict
        Dictionary containing at least the key "machine_id".

    Returns
    -------
    dict
        Updated dictionary with a normalized machine_id.
    """

    id_letters, id_number = machine["machine_id"].split("-")
    id_number_zfilled = id_number.zfill(3)

    machine["machine_id"] = f"{id_letters}-{id_number_zfilled}"

    return machine
