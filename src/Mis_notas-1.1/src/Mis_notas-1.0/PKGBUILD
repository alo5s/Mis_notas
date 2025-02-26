pkgname=mis_notas
pkgver=1.0
pkgrel=1
pkgdesc="Aplicación de gestión de notas en terminal"
arch=('any')
url="https://github.com/alo5s/mis_notas"
license=('MIT')
depends=('python' 'python-rich')
source=("https://github.com/usuario/mis_notas/archive/$pkgver.tar.gz")
sha256sums=('SKIP')

package() {
    install -Dm755 "$srcdir/$pkgname-$pkgver/mis_notas.py" "$pkgdir/usr/bin/mis_notas"
}

