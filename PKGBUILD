pkgname=mis_notas
pkgver=1.0
pkgrel=1
pkgdesc="Aplicación de gestión de notas en terminal"
arch=('any')
url="https://github.com/alo5s/mis_notas"
license=('MIT')
depends=('python' 'python-rich')

# Usando la URL correcta para descargar el repositorio comprimido
#source=("https://github.com/alo5s/Mis_notas/archive/refs/tags/v$pkgver.tar.gz")
source=("https://github.com/alo5s/Mis_notas/archive/refs/tags/v1.0.tar.gz")

# Usando SKIP para evitar la verificación de la suma de verificación mientras no tengamos el archivo
sha256sums=('SKIP')

#package() {
#    install -Dm755 "$srcdir/Mis_notas-$pkgver/mis_notas.py" "$pkgdir/usr/bin/mis_notas"
#}
package() {
    install -Dm755 "$srcdir/Mis_notas-1.0/app.py" "$pkgdir/usr/bin/mis_notas"
}

