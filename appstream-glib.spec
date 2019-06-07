#
# Conditional build:
%bcond_with	alpm		# Arch Linux PacMan support
%bcond_with	stemmer		# search stemmer based on libstemmer
%bcond_without	static_libs	# static libraries

Summary:	GLib Objects and helper methods for reading and writing AppStream metadata
Summary(pl.UTF-8):	Obiekty GLiba i metody pomocnicze do odczytu i zapisu metadanych AppStream
Name:		appstream-glib
Version:	0.7.15
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	https://people.freedesktop.org/~hughsient/appstream-glib/releases/%{name}-%{version}.tar.xz
# Source0-md5:	51f15108d6b9224f2ce2cf9364403b10
Patch0:		%{name}-rpm5.patch
Patch1:		%{name}-stemmer.patch
URL:		https://people.freedesktop.org/~hughsient/appstream-glib/
%{?with_alpm:BuildRequires:	alpm-devel}
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	fontconfig-devel
# pkgconfig(freetype2) >= 9.10.0
BuildRequires:	freetype-devel >= 1:2.2.1
BuildRequires:	gcab-devel >= 1.0
BuildRequires:	gcc >= 5:3.2
BuildRequires:	gdk-pixbuf2-devel >= 2.31.5
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.45.8
BuildRequires:	gobject-introspection-devel >= 0.9.8
BuildRequires:	gperf
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.0
BuildRequires:	json-glib-devel >= 1.1.2
BuildRequires:	libarchive-devel
BuildRequires:	libsoup-devel >= 2.52
BuildRequires:	libstdc++-devel
%{?with_stemmer:BuildRequires:	libstemmer-devel}
BuildRequires:	libuuid-devel
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.37.0
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-devel >= 4.5
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yaml-devel >= 0.1
Requires:	gdk-pixbuf2 >= 2.31.5
Requires:	glib2 >= 1:2.45.8
Requires:	json-glib >= 1.1.2
Requires:	libsoup >= 2.52
Provides:	appdata-tools = %{version}
Obsoletes:	appdata-tools < 0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AppStream-Glib library provides GObjects and helper methods to make it
easy to read and write AppStream metadata. It also provides a simple
DOM implementation that makes it easy to edit nodes and convert to and
from the standardized XML representation.

%description -l pl.UTF-8
Biblioteka AppStream-Glib dostarcza obiekty GLiba (GObject) oraz
metody pomocnicze ułatwiające odczyt i zapis metadanych AppStream.
Zapewnia także prostą implementację DOM ułatwiającą modyfikowanie
węzłów i konwersję do i ze standardowej reprezentacji XML.

%package devel
Summary:	Header files for appstream-glib library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki appstream-glib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gcab-devel >= 1.0
Requires:	gdk-pixbuf2-devel >= 2.31.5
Requires:	glib2-devel >= 1:2.45.8
Requires:	libarchive-devel
Requires:	libuuid-devel
Obsoletes:	appstream-builder-devel < 0.7.15
Obsoletes:	appstream-builder-static < 0.7.15

%description devel
Header files for appstream-glib library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki appstream-glib.

%package static
Summary:	Static appstream-glib library
Summary(pl.UTF-8):	Statyczna biblioteka appstream-glib
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static appstream-glib library.

%description static -l pl.UTF-8
Statyczna biblioteka appstream-glib.

%package apidocs
Summary:	appstream-glib API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki appstream-glib
Group:		Documentation
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
API documentation for appstream-glib library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki appstream-glib.

%package -n bash-completion-appstream-glib
Summary:	Bash completion for appstream-glib package
Summary(pl.UTF-8):	Bashowe dopełnianie składni dla pakietu appstream-glib
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-appstream-glib
Bash completion for appstream-util command.

%description -n bash-completion-appstream-glib -l pl.UTF-8
Bashowe dopełnianie składni polecenia appstream-util.

%package -n appstream-builder
Summary:	AppStreamBuilder library to create AppStream metadata from packages
Summary(pl.UTF-8):	Biblioteka AppStreamBuilder tworząca metadane AppStream z pakietów
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	freetype >= 1:2.2.1

%description -n appstream-builder
AppStreamBuilder library to create AppStream metadata from packages.

%description -n appstream-builder -l pl.UTF-8
Biblioteka AppStreamBuilder tworząca metadane AppStream z pakietów.

%package -n bash-completion-appstream-builder
Summary:	Bash completion for appstream-builder package
Summary(pl.UTF-8):	Bashowe dopełnianie składni dla pakietu appstream-builder
Group:		Applications/Shells
Requires:	appstream-builder = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-appstream-builder
Bash completion for appstream-builder command.

%description -n bash-completion-appstream-builder -l pl.UTF-8
Bashowe dopełnianie składni polecenia appstream-builder.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%if %{with static_libs}
%{__sed} -i -e 's/shared_library/library/' libappstream-glib/meson.build
%endif

%build
# for off64_t
CPPFLAGS="%{rpmcppflags} -D_LARGEFILE64_SOURCE"
%meson build \
	-Dalpm=%{__true_false aplm} \
	-Dstemmer=%{__true_false stemmer} \
	-Dgtk-doc=true

%meson_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install -C build

# already in gettext-tools >= 0.19.7
%{__rm} $RPM_BUILD_ROOT%{_datadir}/gettext/its/appdata.{its,loc}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md
%attr(755,root,root) %{_bindir}/appstream-compose
%attr(755,root,root) %{_bindir}/appstream-util
%attr(755,root,root) %{_libdir}/libappstream-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libappstream-glib.so.8
%{_libdir}/girepository-1.0/AppStreamGlib-1.0.typelib
%{_aclocaldir}/appdata-xml.m4
%{_mandir}/man1/appstream-compose.1*
%{_mandir}/man1/appstream-util.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libappstream-glib.so
%{_datadir}/gir-1.0/AppStreamGlib-1.0.gir
%{_includedir}/libappstream-glib
%{_pkgconfigdir}/appstream-glib.pc
%{_aclocaldir}/appstream-xml.m4

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libappstream-glib.a
%endif

%files -n bash-completion-appstream-glib
%defattr(644,root,root,755)
%{bash_compdir}/appstream-util

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/appstream-glib

%files -n appstream-builder
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/appstream-builder
%dir %{_libdir}/asb-plugins-5
%attr(755,root,root) %{_libdir}/asb-plugins-5/libasb_plugin_appdata.so
%attr(755,root,root) %{_libdir}/asb-plugins-5/libasb_plugin_desktop.so
%attr(755,root,root) %{_libdir}/asb-plugins-5/libasb_plugin_font.so
%attr(755,root,root) %{_libdir}/asb-plugins-5/libasb_plugin_gettext.so
%attr(755,root,root) %{_libdir}/asb-plugins-5/libasb_plugin_hardcoded.so
%attr(755,root,root) %{_libdir}/asb-plugins-5/libasb_plugin_icon.so
%attr(755,root,root) %{_libdir}/asb-plugins-5/libasb_plugin_shell_extension.so
%{_mandir}/man1/appstream-builder.1*

%files -n bash-completion-appstream-builder
%defattr(644,root,root,755)
%{bash_compdir}/appstream-builder
