pkgname=mis_notas
pkgver=1.1
pkgrel=1
pkgdesc="Aplicación de gestión de notas en terminal"
arch=('any')
url="https://github.com/alo5s/mis_notas"
license=('MIT')
depends=('python' 'python-rich')

# Descargar desde el repositorio de GitHub usando el versionado dinámico
source=("https://github.com/alo5s/Mis_notas/archive/refs/tags/v$pkgver.tar.gz")

sha256sums=('SKIP')

package() {
    cd "$srcdir/Mis_notas-$pkgver"
    install -Dm755 "app.py" "$pkgdir/usr/bin/mis_notas"
}

