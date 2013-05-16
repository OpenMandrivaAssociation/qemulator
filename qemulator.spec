%define oname	Qemulator

Summary:	Interface to configure and launch Qemu
Name:		qemulator
Version:	0.5
Release:	%mkrel 9
License:	GPLv2+
Group:		Emulators
URL:		http://qemulator.createweb.de/
Source0:	http://qemulator.createweb.de/%{oname}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		fix_python_dir.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

Requires:	perl-Locale-gettext >= 1.04
Requires:	python
Requires:	pygtk2.0
Requires:	gnome-python
Requires:	qemu
Requires:	pygtk2.0-libglade
BuildRequires:	librsvg
BuildRequires:	libxml2-utils
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pygtk2.0-devel
BuildRequires:	imagemagick

%description
A launcher for Qemu that manages Qemu configs and creates disk images
Qemu-launcher provides a point and click interface to Qemu. It also
allows you to create, save, load, and run multiple Qemu VM
configurations. It has a basic interface for creating or converting
disk images.

Only supports the x86 PC emulator part of Qemu.


%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_datadir}/ \
         %{buildroot}%{_datadir}/%{name} \
         %{buildroot}%{_datadir}/pixmaps \
         %{buildroot}%{_libdir}
cp -a usr/local/lib/qemulator/* %{buildroot}%{_datadir}/qemulator
cp -ra usr/local/share/* %{buildroot}%{_datadir}/
chmod +x %{buildroot}%{_datadir}/qemulator/qml_imagecreation.py \
         %{buildroot}%{_datadir}/qemulator/qml_machinesetup.py \
         %{buildroot}%{_datadir}/qemulator/qml_filehandlers.py \
         %{buildroot}%{_datadir}/qemulator/qml_configuration.py \
         %{buildroot}%{_datadir}/qemulator/qml_tools.py \
         %{buildroot}%{_datadir}/qemulator/qml_installwizzard.py \
         %{buildroot}%{_datadir}/qemulator/qml_style.py
chmod -x %{buildroot}%{_datadir}/qemulator/icons/mac.png
convert -resize 32x32 usr/local/share/pixmaps/qemulator.svg qemulator.xpm
cp qemulator.xpm %{buildroot}%{_datadir}/pixmaps/
ln -s %{_datadir}/qemulator/qemulator.py %{buildroot}%{_bindir}/qemulator

desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/pixmaps/%{name}/%{name}.*
%{_datadir}/locale
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/pixmaps/qemulator/*.png


%changelog
* Mon Aug 06 2012 Johnny A. Solbu <solbu@mandriva.org> 0.5-9mdv2012.0
+ Revision: 811863
- Fix menu entry
- Fix Requires
- Fix License
- Spec cleanup

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.5-8mdv2010.0
+ Revision: 442555
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.5-7mdv2009.1
+ Revision: 350167
- 2009.1 rebuild

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 0.5-6mdv2009.0
+ Revision: 280558
- Remove unneeded BR

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.5-5mdv2009.0
+ Revision: 259912
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.5-4mdv2009.0
+ Revision: 247761
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Mon Mar 31 2008 Anne Nicolas <ennael@mandriva.org> 0.5-2mdv2008.1
+ Revision: 191235
- Add pygtk2.0-libglade require (#39627)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Oct 09 2007 Jérôme Soyer <saispo@mandriva.org> 0.5-1mdv2008.1
+ Revision: 95839
- Add imagemagick to BuildRequires
- Add desktop file
- Add desktop file
- import qemulator


