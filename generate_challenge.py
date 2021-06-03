from generator.generator_data import GeneratorData
import click

from config import Config
from generator.generator import Generator

@click.command()
@click.option('--difficulty',
              type=click.Choice(['easy', 'medium', 'hard'], 
              case_sensitive=False))
@click.option('--challenge', 
              help='Specify a challenge to customise',
              default=None)
@click.option('--multiple', 
              help='How many challenges to generate',
              default=1,
              type=int)
def create_challenge(difficulty, challenge, multiple):

    click.echo(f"Requested {difficulty} challenge.")
    if challenge:
        click.echo(f"Specified challenge: {challenge}")
    click.echo("Generating...")

    generator = Generator(GeneratorData(Config("./config.json")))

    for i in range(0, multiple):
        generated_challenge = generator.generate_challenge(difficulty, challenge)
        print(generated_challenge.get_challenge())

    click.echo("Generation complete!")

if __name__ == '__main__':
    create_challenge()
