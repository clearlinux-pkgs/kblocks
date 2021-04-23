#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kblocks
Version  : 21.04.0
Release  : 30
URL      : https://download.kde.org/stable/release-service/21.04.0/src/kblocks-21.04.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/21.04.0/src/kblocks-21.04.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/21.04.0/src/kblocks-21.04.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: kblocks-bin = %{version}-%{release}
Requires: kblocks-data = %{version}-%{release}
Requires: kblocks-license = %{version}-%{release}
Requires: kblocks-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
EXTENDED

%package bin
Summary: bin components for the kblocks package.
Group: Binaries
Requires: kblocks-data = %{version}-%{release}
Requires: kblocks-license = %{version}-%{release}

%description bin
bin components for the kblocks package.


%package data
Summary: data components for the kblocks package.
Group: Data

%description data
data components for the kblocks package.


%package doc
Summary: doc components for the kblocks package.
Group: Documentation

%description doc
doc components for the kblocks package.


%package license
Summary: license components for the kblocks package.
Group: Default

%description license
license components for the kblocks package.


%package locales
Summary: locales components for the kblocks package.
Group: Default

%description locales
locales components for the kblocks package.


%prep
%setup -q -n kblocks-21.04.0
cd %{_builddir}/kblocks-21.04.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1619206956
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1619206956
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kblocks
cp %{_builddir}/kblocks-21.04.0/COPYING %{buildroot}/usr/share/package-licenses/kblocks/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/kblocks-21.04.0/COPYING.DOC %{buildroot}/usr/share/package-licenses/kblocks/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
pushd clr-build
%make_install
popd
%find_lang kblocks

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kblocks

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kblocks.desktop
/usr/share/config.kcfg/kblocks.kcfg
/usr/share/icons/hicolor/128x128/apps/kblocks.png
/usr/share/icons/hicolor/16x16/apps/kblocks.png
/usr/share/icons/hicolor/22x22/apps/kblocks.png
/usr/share/icons/hicolor/32x32/apps/kblocks.png
/usr/share/icons/hicolor/48x48/apps/kblocks.png
/usr/share/icons/hicolor/64x64/apps/kblocks.png
/usr/share/kblocks/sounds/block-fall.ogg
/usr/share/kblocks/sounds/block-move.ogg
/usr/share/kblocks/sounds/block-remove.ogg
/usr/share/kblocks/themes/default.desktop
/usr/share/kblocks/themes/default_block_fall.ogg
/usr/share/kblocks/themes/default_block_move.ogg
/usr/share/kblocks/themes/egyptian.svg
/usr/share/kblocks/themes/egyptian_preview.png
/usr/share/kblocks/themes/oxygen.desktop
/usr/share/kblocks/themes/oxygen.svg
/usr/share/kblocks/themes/oxygen_preview.png
/usr/share/knsrcfiles/kblocks.knsrc
/usr/share/kxmlgui5/kblocks/kblocksui.rc
/usr/share/metainfo/org.kde.kblocks.appdata.xml
/usr/share/qlogging-categories5/kblocks.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/kblocks/index.cache.bz2
/usr/share/doc/HTML/de/kblocks/index.docbook
/usr/share/doc/HTML/en/kblocks/gameboard.png
/usr/share/doc/HTML/en/kblocks/index.cache.bz2
/usr/share/doc/HTML/en/kblocks/index.docbook
/usr/share/doc/HTML/es/kblocks/index.cache.bz2
/usr/share/doc/HTML/es/kblocks/index.docbook
/usr/share/doc/HTML/et/kblocks/index.cache.bz2
/usr/share/doc/HTML/et/kblocks/index.docbook
/usr/share/doc/HTML/fr/kblocks/index.cache.bz2
/usr/share/doc/HTML/fr/kblocks/index.docbook
/usr/share/doc/HTML/gl/kblocks/index.cache.bz2
/usr/share/doc/HTML/gl/kblocks/index.docbook
/usr/share/doc/HTML/it/kblocks/index.cache.bz2
/usr/share/doc/HTML/it/kblocks/index.docbook
/usr/share/doc/HTML/nl/kblocks/index.cache.bz2
/usr/share/doc/HTML/nl/kblocks/index.docbook
/usr/share/doc/HTML/pl/kblocks/index.cache.bz2
/usr/share/doc/HTML/pl/kblocks/index.docbook
/usr/share/doc/HTML/pt/kblocks/index.cache.bz2
/usr/share/doc/HTML/pt/kblocks/index.docbook
/usr/share/doc/HTML/pt_BR/kblocks/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kblocks/index.docbook
/usr/share/doc/HTML/sv/kblocks/index.cache.bz2
/usr/share/doc/HTML/sv/kblocks/index.docbook
/usr/share/doc/HTML/uk/kblocks/gameboard.png
/usr/share/doc/HTML/uk/kblocks/index.cache.bz2
/usr/share/doc/HTML/uk/kblocks/index.docbook

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kblocks/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/kblocks/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f kblocks.lang
%defattr(-,root,root,-)

