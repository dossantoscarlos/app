use std::io;
extern crate unicode_normalization;
use unicode_normalization::UnicodeNormalization;

fn verifica_palindromo(texto_processado: &str, texto_original: &str) {
    let texto_original = texto_original.trim().split_whitespace();
    let palavras = texto_processado.trim().split_whitespace();

    for (texto_original, palavras) in texto_original.zip(palavras) {
        println!("{}", message(palavras, texto_original));
    }
}

fn message(palavras: &str, texto_original: &str) -> String {
    if palavras == palavras.chars().rev().collect::<String>() {
        return format!("{} : é palíndromo", texto_original);
    }
    format!("{} : não é palíndromo", texto_original)
}

fn remove_unicode(texto: &str) -> String {
    let texto_normalizado = texto.nfkd().collect::<String>();
    let texto_sem_acentos: String = texto_normalizado.chars()
        .filter(|c| c.is_alphabetic() || c.is_whitespace())
        .collect();
    texto_sem_acentos
}

fn valida_exit() -> bool {
    let mut option = String::new();
    println!("Deseja continuar? Digite S ou N: ");
    io::stdin().read_line(&mut option).expect("Falha ao ler a entrada");
    let option = option.trim().to_lowercase();
    if option != "s" && option != "n" {
        return valida_exit();
    }
    finaliza_program(&option)
}

fn finaliza_program(option: &str) -> bool {
    option == "n"
}

fn execute() {
    loop {
        let mut texto_original = String::new();
        println!("Digite uma frase ou palavra/número: ");
        io::stdin().read_line(&mut texto_original).expect("Falha ao ler a entrada");
        verifica_palindromo(&remove_unicode(&texto_original), &texto_original);
        if valida_exit() {
            break;
        }
    }
}

fn main() {
    execute();
}
