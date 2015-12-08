#
# Conditional build:
%bcond_without	ostree	# ostree support
%bcond_with	alpm	# Arch Linux PacMan support

Summary:	GLib Objects and helper methods for reading and writing AppStream metadata
Summary(pl.UTF-8):	Obiekty GLiba i metody pomocnicze do odczytu i zapisu metadanych AppStream
Name:		appstream-glib
Version:	0.5.4
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://people.freedesktop.org/~hughsient/appstream-glib/releases/%{name}-%{version}.tar.xz
# Source0-md5:	894f5a2d0d8ff8d5021304b1ddd2b0a7
Patch0:		%{name}-rpm5.patch
Patch1:		%{name}-pc.patch
URL:		http://people.freedesktop.org/~hughsient/appstream-glib/
%{?with_alpm:BuildRequires:	alpm-devel}
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.9
BuildRequires:	docbook-dtd43-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	fontconfig-devel
# pkgconfig(freetype2) >= 9.10.0
BuildRequires:	freetype-devel >= 1:2.2.1
BuildRequires:	gcab-devel
BuildRequires:	gdk-pixbuf2-devel >= 2.31.5
BuildRequires:	gettext-tools >= 0.17
BuildRequires:	glib2-devel >= 1:2.45.8
BuildRequires:	gobject-introspection-devel >= 0.9.8
BuildRequires:	gperf
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libarchive-devel
BuildRequires:	libsoup-devel >= 2.52
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2
BuildRequires:	libxslt-progs
%{?with_ostree:BuildRequires:	ostree-devel >= 2015.1}
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	rpm-devel >= 4.5
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yaml-devel
Requires:	gdk-pixbuf2 >= 2.31.5
Requires:	glib2 >= 1:2.45.8
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
Requires:	gdk-pixbuf2-devel >= 2.31.5
Requires:	glib2-devel >= 1:2.45.8

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

%package -n appstream-builder-devel
Summary:	Header files for AppStreamBuilder library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki AppStreamBuilder
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	appstream-builder = %{version}-%{release}

%description -n appstream-builder-devel
Header files for AppStreamBuilder library.

%description -n appstream-builder-devel -l pl.UTF-8
Pliki nagłówkowe biblioteki AppStreamBuilder.

%package -n appstream-builder-static
Summary:	Static AppStreamBuilder library
Summary(pl.UTF-8):	Statyczna biblioteka AppStreamBuilder
Group:		Development/Libraries
Requires:	appstream-builder-devel = %{version}-%{release}

%description -n appstream-builder-static
Static AppStreamBuilder library.

%description -n appstream-builder-static -l pl.UTF-8
Statyczna biblioteka AppStreamBuilder.

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

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_alpm:--enable-alpm} \
	%{!?with_ostree:--disable-ostree} \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/asb-plugins-4/lib*.{la,a}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libappstream-*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	-n appstream-builder -p /sbin/ldconfig
%postun	-n appstream-builder -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md
%attr(755,root,root) %{_bindir}/appstream-util
%attr(755,root,root) %{_libdir}/libappstream-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libappstream-glib.so.8
%{_libdir}/girepository-1.0/AppStreamGlib-1.0.typelib
%{_aclocaldir}/appdata-xml.m4
%{_mandir}/man1/appstream-util.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libappstream-glib.so
%{_datadir}/gir-1.0/AppStreamGlib-1.0.gir
%{_includedir}/libappstream-glib
%{_pkgconfigdir}/appstream-glib.pc
%{_aclocaldir}/appstream-xml.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libappstream-glib.a

%files -n bash-completion-appstream-glib
%defattr(644,root,root,755)
%{bash_compdir}/appstream-util

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/appstream-glib

%files -n appstream-builder
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/appstream-builder
%attr(755,root,root) %{_libdir}/libappstream-builder.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libappstream-builder.so.8
%{_libdir}/girepository-1.0/AppStreamBuilder-1.0.typelib
%dir %{_libdir}/asb-plugins-4
%attr(755,root,root) %{_libdir}/asb-plugins-4/libasb_plugin_absorb.so
%attr(755,root,root) %{_libdir}/asb-plugins-4/libasb_plugin_appdata.so
%attr(755,root,root) %{_libdir}/asb-plugins-4/libasb_plugin_dbus.so
%attr(755,root,root) %{_libdir}/asb-plugins-4/libasb_plugin_desktop.so
%attr(755,root,root) %{_libdir}/asb-plugins-4/libasb_plugin_font.so
%attr(755,root,root) %{_libdir}/asb-plugins-4/libasb_plugin_gettext.so
%attr(755,root,root) %{_libdir}/asb-plugins-4/libasb_plugin_gir.so
%attr(755,root,root) %{_libdir}/asb-plugins-4/libasb_plugin_gresource.so
%attr(755,root,root) %{_libdir}/asb-plugins-4/libasb_plugin_gstreamer.so
%attr(755,root,root) %{_libdir}/asb-plugins-4/libasb_plugin_hardcoded.so
%attr(755,root,root) %{_libdir}/asb-plugins-4/libasb_plugin_kde_notifyrc.so
%attr(755,root,root) %{_libdir}/asb-plugins-4/libasb_plugin_kde_services.so
%attr(755,root,root) %{_libdir}/asb-plugins-4/libasb_plugin_nm.so
%if %{with ostree}
%attr(755,root,root) %{_libdir}/asb-plugins-4/libasb_plugin_ostree.so
%endif
%{_mandir}/man1/appstream-builder.1*

%files -n appstream-builder-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libappstream-builder.so
%{_includedir}/libappstream-builder
%{_datadir}/gir-1.0/AppStreamBuilder-1.0.gir
%{_pkgconfigdir}/appstream-builder.pc

%files -n appstream-builder-static
%defattr(644,root,root,755)
%{_libdir}/libappstream-builder.a

%files -n bash-completion-appstream-builder
%defattr(644,root,root,755)
%{bash_compdir}/appstream-builder
