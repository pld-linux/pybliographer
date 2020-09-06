Summary:	Framework for working with bibliographic databases
Summary(pl.UTF-8):	Szkielet do pracy z bibliograficznymi bazami danych
Name:		pybliographer
Version:	1.4.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/pybliographer/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	3b979bc54ce746303cd38df0c0c60edb
URL:		https://pybliographer.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-pygtk-devel >= 2:2.24.0
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	python-bibtex >= 1.2.7
Requires:	python-pygtk-gtk >= 2:2.24.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pybliographer provides a framework for working with bibliographic
databases.

%description -l pl.UTF-8
Pybliographer dostarcza szkielet do pracy z bibliograficznymi bazami
danych.

%prep
%setup -q

%build
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	PYTHON="%{__python}" \
	--disable-depchecks \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database
%update_icon_cache hicolor

%postun
%update_desktop_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/pybliocheck
%attr(755,root,root) %{_bindir}/pybliocompact
%attr(755,root,root) %{_bindir}/pyblioconvert
%attr(755,root,root) %{_bindir}/pyblioformat
%attr(755,root,root) %{_bindir}/pybliographer
%attr(755,root,root) %{_bindir}/pybliographic
%attr(755,root,root) %{_bindir}/pybliotex
%attr(755,root,root) %{_bindir}/pybliotext
%{_datadir}/pybliographer
%{_datadir}/appdata/pybliographic.appdata.xml
%{_desktopdir}/pybliographic.desktop
%{_iconsdir}/hicolor/*x*/apps/pybliographic.png
%{_iconsdir}/hicolor/scalable/apps/pybliographic.svg
