Summary:	GLib Objects and helper methods for reading and writing AppStream metadata
Summary(pl.UTF-8):	Obiekty GLiba i metody pomocnicze do odczytu i zapisu metadanych AppStream
Name:		appstream-glib
Version:	0.1.7
Release:	1
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://people.freedesktop.org/~hughsient/appstream-glib/releases/%{name}-%{version}.tar.xz
# Source0-md5:	4779c8b21df42cb0e874478201cee419
URL:		http://people.freedesktop.org/~hughsient/appstream-glib/
BuildRequires:	gdk-pixbuf2-devel >= 2.14
BuildRequires:	glib2-devel >= 1:2.16.1
BuildRequires:	gobject-introspection-devel >= 0.9.8
BuildRequires:	gperf
BuildRequires:	gtk-doc >= 1.9
BuildRequires:	libarchive-devel
BuildRequires:	libsoup-devel >= 2.24
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.16.1
Requires:	gdk-pixbuf2 >= 2.14
Requires:	libsoup >= 2.24
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
Requires:	gdk-pixbuf2-devel >= 2.14
Requires:	glib2-devel >= 1:2.16.1

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

%description apidocs
API documentation for appstream-glib library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki appstream-glib.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libappstream-glib.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS MAINTAINERS NEWS README.md
%attr(755,root,root) %{_bindir}/appstream-util
%attr(755,root,root) %{_libdir}/libappstream-glib.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libappstream-glib.so.1
%{_libdir}/girepository-1.0/AppStreamGlib-1.0.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libappstream-glib.so
%{_datadir}/gir-1.0/AppStreamGlib-1.0.gir
%{_includedir}/libappstream-glib
%{_pkgconfigdir}/appstream-glib.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libappstream-glib.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/appstream-glib
