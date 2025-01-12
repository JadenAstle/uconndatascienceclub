'''This is an information file for uconndatascienceclub. This file should include basic commands that give club information.''' 

class info():

    def __init__(self):
        self.uconntact = 'https://uconntact.uconn.edu/organization/datascience'
        self.instagram = '@uconndatascience'
        self.email = 'uconndatascience@gmail.com'
        self.discord = 'https://discord.gg/zTTYvVAa'

    def welcome():
        '''Get a welcome message to ensure package is working properly.
        
        Returns
        -------
        str
            A welcome string.
        '''
        return 'Welcome to UConn Data Science Club!'


    def schedule(year: int=2025, semester: str='spring') -> dict:
        '''
        Get the schedule for the specified year and semester.

        Parameters
        ----------
        year : int, optional
            The academic year. Must be one of {2024, 2025}. Default is 2025 (current year).
        semester : str, optional
            The academic semester. Must be one of {'spring', 'fall'}. Default is 'spring'.

        Returns
        -------
        dict
            A dictionary representing the schedule for the given year and semester.
        '''
        # Implementation goes here
        pass


